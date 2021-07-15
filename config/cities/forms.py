from django import forms
from .models import City


class CityCreateForm(forms.ModelForm):
    title = forms.CharField(label='City', widget=forms.TextInput(attrs={
        'placeholder': 'Enter the name of the city'
    }))

    class Meta:
        model = City
        fields = ['title']