from django import forms
from .models import Train
from cities.models import City


class TrainCreateForm(forms.ModelForm):
    number = forms.CharField(label='Train №', widget=forms.TextInput(attrs={
        'placeholder': 'Enter the number of the train'
    }))
    travel_time = forms.IntegerField(min_value=1)
    from_city = forms.ModelChoiceField(queryset=City.get_all_cities())
    to_city = forms.ModelChoiceField(queryset=City.get_all_cities())

    class Meta:
        model = Train
        fields = ['number', 'travel_time', 'from_city', 'to_city']