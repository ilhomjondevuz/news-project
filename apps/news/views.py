from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .forms import ContactForm
from .models import Newness


def news_list_view(request):
    news = Newness.objects.all()
    context = {'news': news}
    return render(request, 'news/news_list.html', context)

def news_detail_view(request, slug):
    newness = get_object_or_404(Newness, slug=slug)
    context = {'newness': newness}
    return render(request, 'news/news_detail.html', context)

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
            return redirect('news:contact')
        else:
            messages.error(request, "❌ Xabar yuborishda xatolik yuz berdi.")
        return render(request, self.template_name, {'form': form})