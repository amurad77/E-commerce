from django.views.generic.base import TemplateView
from product.models import Brand, Category, Product
from django.views.generic.list import ListView
from core.models import Contact
from django.views.generic.edit import CreateView
from core.forms import ContactForm



class NotFoundView(TemplateView):
    template_name = "404.html"


class AboutPageView(TemplateView):
    template_name = "about-page.html"


class CreateContactView(CreateView):
    template_name = 'contact.html' 
    model = Contact
    success_url = '/contact'
    form_class = ContactForm 


class FaqView(TemplateView):
    template_name = "faq.html"


class ProductListView(ListView): 
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.filter(is_published=True)
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Product.objects.filter(is_published = True).order_by("-created_at")[:6]
        context['sale_products'] = Product.objects.exclude(discount = None).filter(is_published = True).order_by("-created_at")[:6]
        context['category_list'] = Category.objects.filter(parent_cat=None)
        context ['brand_list']  = Brand.objects.all()
        return context