from django.urls import reverse_lazy

from .models import Person
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import PersonForm


class PersonDetail(DetailView):
    model = Person
    template_name = 'person/person_detail.html'
    context_object_name = 'person'


class PersonUpdate(UpdateView):
    model = Person
    template_name = 'person/person_update.html'
    form_class = PersonForm
    success_url = reverse_lazy('person_list')


class PersonDelete(DeleteView):
    model = Person
    success_url = '/person'
    template_name = 'person/person_del.html'


def create_person(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
        else:
            error = "Форма была неверной"

    form = PersonForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'person/person_create.html', data)


def person_list(request):
    person = Person.objects.all()
    return render(request, 'person/person_list.html', {'person': person})




