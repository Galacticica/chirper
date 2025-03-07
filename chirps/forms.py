"""
File: forms.py
Author: Reagan Zierke
Date: 3/6/2025
Description: Creates forms for the chirps app.
"""


from django import forms
from .models import Chirp, Reply

class ChirpForm(forms.ModelForm):
    '''
    A form for writing new chirps. It uses hidden input to allow for Trix to use rich text.
    '''
    class Meta:
        model = Chirp
        fields = ['content']
        widgets = {
            'content': forms.HiddenInput(), 
        }

class LikeForm(forms.Form):
    '''
    Form for liking chirps.
    '''
    chirp_id = forms.IntegerField(widget=forms.HiddenInput())

class ReplyForm(forms.ModelForm):
    '''
    A form for writing new replies to chirps. It uses hidden input to allow for Trix to use rich text.
    '''
    class Meta:
        model = Reply
        fields = ['content']
        widgets = {
            'content': forms.HiddenInput(), 
        }


