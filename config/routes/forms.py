from django import forms
from cities.models import City


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(queryset=City.get_all_cities())
    to_city = forms.ModelChoiceField(queryset=City.get_all_cities())
    through_cities = forms.ModelMultipleChoiceField(queryset=City.objects.all(), required=False,
                                                    widget=forms.SelectMultiple)
