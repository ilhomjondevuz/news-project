from django.urls import path

from .views import RegisterView, custom_login_view, CustomLoginView, custom_logout_view, CustomLogoutView, \
    UserProfileView, UserUpdateView, CustomPasswordChangeView, customPasswordChangeDoneView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile_update'),
    path('profile/change_password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('profile/change_password/done/', customPasswordChangeDoneView.as_view(), name='password_change_done'),
]