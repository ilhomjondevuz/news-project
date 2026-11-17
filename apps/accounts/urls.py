from django.urls import path

from .views import RegisterView, CustomLoginView, logout_view, CustomUserChangeView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/update/', CustomUserChangeView.as_view(), name='profile'),
]