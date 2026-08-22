from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from hitcount.views import HitCountMixin

from .forms import ContactForm, NewnessForm
from .models import Newness, Category


def news_list_view(request):
    news = Newness.objects.all()
    context = {'news': news}
    return render(request, 'news/news_list.html', context)

def news_detail_view(request, slug):
    newness = get_object_or_404(Newness, slug=slug)
    context = {'newness': newness}
    return render(request, 'news/news_detail.html', context)


class NewnessDetailView(generic.DetailView):
    model = Newness
    template_name = 'news/detail.html'
    context_object_name = 'newness'


# def contact_view(request):
#     form = ContactForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('news:contact')
#     return render(request, 'partials/contact_form.html', context=context)

class ContactView(generic.TemplateView):
    template_name = 'partials/contact_form.html'
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect('contact')
        else:
            messages.error(request, "❌ Xabar yuborishda xatolik yuz berdi.")
        return render(request, self.template_name, {'form': form})

class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Newness.objects.all()

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'news/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category = Category.objects.filter(slug=self.kwargs['slug']).first()
        news = Newness.published_objects.filter(category=category)
        context['news'] = news
        context['category'] = category
        return context

class NewsUpdateView(generic.UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Newness
    template_name = 'news/news_update.html'
    context_object_name = 'news'
    form_class = NewnessForm

    def test_func(self):
        return self.request.user.is_authenticated