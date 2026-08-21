from django.urls import path

from .views import news_list_view, news_detail_view, contact_view

urlpatterns = [
    path('', news_list_view, name='news_list'),
    path('news/<slug:slug>', news_detail_view, name='news_detail'),
    path('contact/', contact_view, name='contact'),
]