from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import RegistrationForm, LoginForm, CustomUserChangeForm
from .models import Account


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('accounts:login')

class CustomLoginView(LoginView):
    # form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('news:home')

    def get_success_url(self):
        return self.request.POST.get('next') or self.request.GET.get('next') or reverse_lazy('news:home')

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'), 'news:home')

class CustomUserChangeView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = CustomUserChangeForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user