from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'review']
        labels = {
            'title': 'Название фильма',
            'description': 'Описание фильма',
            'review': 'Отзыв'
        }
