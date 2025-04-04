from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_view.html'
    context_object_name = 'news'

class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news'
    template_name = 'news/news-delete.html'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/create_news.html'
    success_url = reverse_lazy('news_home')
    form_class = NewsForm

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма была неверной"

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create_news.html', data)


