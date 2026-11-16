from django.views.generic import CreateView

from .forms import RegistrationForm


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = '/accounts/login/'