from django.forms import ModelForm, TextInput, FileInput, Textarea, NumberInput
from .models import MapInfo

class CreateMap(ModelForm):
    class Meta:
        model = MapInfo
        fields = ['name', 'latitude', 'longitude', 'icons', 'history', 'photos']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование объекта или места'
            }),
            "latitude": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Широта'
            }),
            "longitude": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Долгота'
            }),
            "icons": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иконки'
            }),
            "history": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'История места'
            }),
            "photos": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фотографии'
            })
        }
