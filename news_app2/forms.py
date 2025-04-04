from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['name', 'anons', 'date', 'text2', 'photo']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "text2": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "photo": FileInput(attrs={
                'class': 'form-control'
            })
        }

