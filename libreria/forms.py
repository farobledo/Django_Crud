
from django import forms
from .models import libro


class libroFrom(forms.ModelForm):
    class Meta:
        model = libro
        fields = '__all__'
