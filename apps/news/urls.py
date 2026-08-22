from django.urls import path

from .views import NewnessDetailView, ContactView, HomePageView, CategoryDetailView, NewsUpdateView, NewnessDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/<slug:slug>', NewnessDetailView.as_view(), name='news_detail'),
    path('news/<slug:slug>/update', NewsUpdateView.as_view(), name='newsness_update'),
    path('news/<slug:slug>/delete', NewnessDeleteView.as_view(), name='newsness_delete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('categories/<slug:slug>/',CategoryDetailView.as_view(), name='category_detail'),
]