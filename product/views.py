import django
from django.views.generic.list import ListView
from product.forms import ReviewForm
from product.models import Category, Product, Review,Brand
from django.views.generic import DetailView,ListView
from django.views.generic.edit import  FormView
from order.models import ProductWishlist
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Min,Max



class ProductDetailView(FormView, DetailView):
    model = Product
    template_name = 'product-page.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent_cat=None)
        context ['products'] = Product.objects.filter(is_published = True)
        context['new_products'] = Product.objects.filter(is_published = True).order_by("created_at")[:6]
        context['related_products'] = Product.objects.filter(category=self.get_object().category).exclude(id=self.get_object().id)
        if self.request.user.is_authenticated:
            in_wish = ProductWishlist.objects.filter(wishlist=self.request.user.wishlist,product=self.get_object()).first()
            if in_wish:
                context['in_wishlist'] = in_wish.pk
            else:
                context['in_wishlist'] = False
        context['review'] = Review.objects.all().order_by('-created_at') 

        return context

    def get_success_url(self):
        return f'/product/{self.get_object().id}'

    def form_valid(self, form):
        rev = form.save(commit=False)
        rev.product = self.get_object()
        rev.save()
        return super().form_valid(form)

    
class ProductListView(ListView):
    model = Product
    template_name = 'category-page.html'
    queryset = Product.objects.filter(is_published=True)
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Product.objects.filter(is_published = True).order_by("-created_at")[:6]
        context['category_list'] = Category.objects.filter(parent_cat=None)
        context ['brand_list']  = Brand.objects.all()
        minMaxPrice = self.model.objects.aggregate(Min('price'),Max('price'))
        minMaxPrice['price__min']=int(minMaxPrice['price__min'])
        minMaxPrice['price__max']=int(minMaxPrice['price__max'])
        context['minMaxPrice'] = minMaxPrice
        
        return context


class SearchResultsView(ListView):
    model = Product
    template_name = 'search.html'

    def get_queryset(self): 
        query = self.request.GET.get('m')
        object_list = Product.objects.filter(title__icontains=query)
        return object_list



def filter_data(request):
    
    size = request.GET.getlist('Size[]')
    brand = request.GET.getlist('Brand[]')
    # category = request.GET.getlist('Category[]')
    maxPrice = request.GET['maxPrice']
    minPrice = request.GET['minPrice']

    allproducts = Product.objects.all().order_by('-id')
    allproducts=allproducts.filter(price__lte=maxPrice)
    allproducts=allproducts.filter(price__gte=minPrice)
    if len(size)>0:
    	allproducts=allproducts.filter(productattribute__in=size).distinct()
    if len(brand)>0:
        allproducts=allproducts.filter(brand__in=brand).distinct()

    # if len(category)>0:
    #     allproducts=allproducts.filter(category__in=category).distinct()
    t = render_to_string('product.html',{'data':allproducts})
    return JsonResponse({'data':t})







