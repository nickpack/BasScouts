__author__ = 'Nick Pack'
from django import forms

class ContactForm(forms.Form):
    sender_name = message = forms.CharField()
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.widgets.Textarea())
    cc_myself = forms.BooleanField(required=False)