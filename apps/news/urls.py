from django.urls import path

from .views import NewsDetailView, ContactView, HomePageView, CategoryDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/<slug:slug>', NewsDetailView.as_view(), name='news_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('categories/<slug:slug>/',CategoryDetailView.as_view(), name='category_detail'),
]