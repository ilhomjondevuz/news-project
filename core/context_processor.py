from apps.news.models import Category, Newness


def categories_context_processor(request):
    categories = Category.objects.all()
    latest_news = Newness.published_objects.all().order_by('-published_at')[:5]
    context = {
        'categories': categories,
        'latest_news': latest_news,
    }
    return context