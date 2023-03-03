from django import forms
from django.forms import ModelForm
from .models import Events


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ['item']
        item = forms.CharField()