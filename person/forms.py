from django import forms
from .models import Person
from django.forms import TextInput, Textarea, FileInput

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'post', 'role', 'history', 'image', 'photo1']  # Use a list instead of a set

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя участника'
            }),
            "post": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место работы/учебы участника'
            }),
            "role": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Роль участника в экспедиции'
            }),
            "history": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'История участника'
            }),
            'image': FileInput(attrs={
                'class': 'form-control'
            }),
            'photo1': FileInput(attrs={
                'class': 'form-control'
            })
        }
