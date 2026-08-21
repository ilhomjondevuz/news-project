from django.shortcuts import render, get_object_or_404

from .models import Newness


def news_list_view(request):
    news = Newness.objects.all()
    context = {'news': news}
    return render(request, 'news/news_list.html', context)

def news_detail_view(request, slug):
    newness = get_object_or_404(Newness, slug=slug)
    context = {'newness': newness}
    return render(request, 'news/news_detail.html', context)

def contact_view(request):
    context = {

    }
    return render(request, 'contact.html', context=context)