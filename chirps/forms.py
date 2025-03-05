from django import forms
from .models import Chirp

class ChirpForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        max_length=255,
        widget=forms.Textarea(attrs={'placeholder': 'Write a new chirp...'}
    ))

    class Meta:
        model = Chirp
        fields = ['content']

    