from django.urls import path

from .views import news_list_view, news_detail_view

urlpatterns = [
    path('', news_list_view, name='news_list'),
    path('news/<slug:slug>', news_detail_view, name='news_detail'),
]