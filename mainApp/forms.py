
from django import forms


class videoconversionform(forms.Form):
    links = forms.CharField()
    mail_address = forms.EmailField()
