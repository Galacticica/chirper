from django import forms
from .models import Chirp, Reply

class ChirpForm(forms.ModelForm):
    class Meta:
        model = Chirp
        fields = ['content']
        widgets = {
            'content': forms.HiddenInput(), 
        }

class LikeForm(forms.Form):
    chirp_id = forms.IntegerField(widget=forms.HiddenInput())

class ReplyForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        max_length=255,
        widget=forms.Textarea(attrs={'placeholder': 'Write a reply...'})
    )

    class Meta:
        model = Reply
        fields = ['content']


