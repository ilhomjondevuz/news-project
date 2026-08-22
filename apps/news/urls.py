from django.urls import path

from .views import NewnessDetailView, ContactView, HomePageView, CategoryDetailView, NewsUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/<slug:slug>', NewnessDetailView.as_view(), name='news_detail'),
    path('news/<slug:slug>/update', NewsUpdateView.as_view(), name='newsness_update'),  # shu tugadi. Endi news deailda update qilish avval detailni chiqarish
    path('contact/', ContactView.as_view(), name='contact'),
    path('categories/<slug:slug>/',CategoryDetailView.as_view(), name='category_detail'),
]