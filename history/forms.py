from django.forms import ModelForm

from .models import History
from django.forms import TextInput, Textarea, IntegerField, FileInput
class CreateMap(ModelForm):
    class Meta:
        model = History
        fields = ['name', 'text', 'number', 'image']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'История'
            }),
            "number": IntegerField(attrs={
                'class': 'form-control',
                'placeholder': 'Дата фотографий'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фото для прервью'
            })
        }