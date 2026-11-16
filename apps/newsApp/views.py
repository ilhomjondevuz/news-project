from django.shortcuts import render

from .models import Category


def home_view(request):
    return render(request, 'home.html')

def categories_list_view(request):
    categories = Category.objects.all()
    return render(request, 'newsApp/categories_list_view.html', {'categories': categories})