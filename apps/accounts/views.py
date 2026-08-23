from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.utils.translation import gettext_lazy as _

from .forms import RegisterForm, LoginForm


User = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

def custom_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, _('Username or password is incorrect.'))
            elif not user.is_active:
                messages.error(request, _('Your account is inactive.'))
            else:
                login(request, user)
                return redirect('home')
            return redirect('login')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def custom_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))