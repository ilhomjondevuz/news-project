from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

from .forms import LoginForm, UserForm, UserChangeForm

User = get_user_model()

class RegisterView(CreateView):
    form_class = UserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        messages.success(self.request, _('Registration successful.'))
        return response

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.success(self.request, _('Login successful.'))
        return reverse_lazy('home')

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

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('home')
    http_method_names = ['get', 'post']

class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    form_class = UserForm
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

    def get_object(self, *args, **kwargs):
        return self.request.user

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'accounts/profile_update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('profile')

    def get_object(self, *args, **kwargs):
        return self.request.user

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('password_change_done')

class customPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'