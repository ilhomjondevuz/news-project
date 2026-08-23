from django.urls import path

from .views import RegisterView, custom_login_view, CustomLoginView, custom_logout_view, CustomLogoutView, \
    UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]