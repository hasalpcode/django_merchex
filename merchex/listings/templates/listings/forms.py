from dataclasses import fields
from pyexpat import model
from django import forms

from listings.models import Band

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        