from django.shortcuts import render
from django.views.generic import DetailView
from .models import History
from django.core.paginator import Paginator

def history_list(request):
    history = History.objects.all()
    paginator = Paginator(history, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "history/history_list.html", {'history': page_obj })

class DetailHistory(DetailView):
    model = History
    template_name = 'history/history.html'
    context_object_name = 'history'




