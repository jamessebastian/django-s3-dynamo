from django import forms
from .models import Flick

class FlickForm(forms.ModelForm):
    class Meta:
        model = Flick
        fields = ('title','description','tags', 'picture')

