from django.urls import path

from .views import (news_detail_view, ContactView, HomePageView, CategoryDetailView, NewsUpdateView, NewnessDeleteView,
                    NewsCreateView, NewsHitDetailView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:slug>/', news_detail_view, name='news_detail'),
    path('news/<slug:slug>/update/', NewsUpdateView.as_view(), name='newsness_update'),
    path('news/<slug:slug>/delete/', NewnessDeleteView.as_view(), name='newsness_delete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('categories/<slug:slug>/',CategoryDetailView.as_view(), name='category_detail'),
]