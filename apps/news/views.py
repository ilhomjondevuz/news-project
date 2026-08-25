from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import ContactForm, NewnessForm
from .models import Newness, Category


def news_list_view(request):
    news = Newness.objects.all()
    context = {'news': news}
    return render(request, 'news/news_list.html', context)

def news_detail_view(request, slug):
    newness = get_object_or_404(Newness.published_objects.all(), slug=slug)
    context = {'newness': newness}
    return render(request, 'news/detail.html', context)


class NewnessDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView
):
    model = Newness
    template_name = 'news/delete.html'
    context_object_name = 'newness'

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.delete()
        return redirect('home')


class NewsCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Newness
    form_class = NewnessForm
    template_name = 'news/news_create.html'
    context_object_name = 'newness'

    def test_func(self):
        return self.request.user.is_staff


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
        return Newness.published_objects.all()

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