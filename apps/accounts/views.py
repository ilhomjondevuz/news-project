from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .forms import RegisterForm, LoginForm


User = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(
            self.request,
            username=username,
            password=password,
        )

        if user is None:
            form.add_error(
                None,
                'Username yoki password noto‘g‘ri.'
            )
            return self.form_invalid(form)

        login(self.request, user)

        return super().form_valid(form)

def custom_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))