from account.forms import CustomSetPasswordForm, LoginForm, RegisterForm, CustomPasswordResetForm,MyPasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as django_login , logout as django_logout
from django.contrib import messages
from django.urls import reverse_lazy
from account.tasks import send_confirmation_mail
from account.utils.token import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView,PasswordChangeView
from order.models import Wishlist,Cart


User = get_user_model()


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kvargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(CustomLoginView, self).dispatch(request, *args, **kvargs)



def logout(request):
    django_logout(request)
    return redirect (reverse_lazy('account:login'))
    
class ProfileView(TemplateView):
    template_name = "profile.html"



class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'email/password_reset_email.html'
    form_class = CustomPasswordResetForm
    template_name = 'forget_pwd.html'
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Muracietiniz gabul oldu, emaile baxin zehmet olmasa')
        return super(CustomPasswordResetView, self).get_success_url()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Sifreniz ugurla deyisdi')
        return super(CustomPasswordResetConfirmView, self).get_success_url()


class MyPasswordChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Sifreniz ugurla deyisdirildi')
        return super(MyPasswordChangeView, self).get_success_url()
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('account:login')

    def dispatch(self, request, *args, **kvargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kvargs)

    def form_valid(self, form):
        form.instance.is_active = False
        result = super().form_valid(form)
        user = form.instance
        Cart.objects.create(user=user)
        Wishlist.objects.create(user=user)
        send_confirmation_mail(user)
        messages.success(self.request, ' Qeydiyyatdan ugurla kecdiniz emaile baxib testiq edin zehmet olmasa')
        return result


def activate(request, uidb64, token):

    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()


    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Your account activated')
        user.is_active = True
        user.save()
        logout(request)
        return redirect('account:login')
    else:
        messages.error(request, 'Invalid error')
        return redirect('account:register')



class VendorView(TemplateView):
    template_name = 'vendor-profile.html'








