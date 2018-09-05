
from django import forms


class VideoConversionForm(forms.Form):
    links = forms.CharField()
    mail_address = forms.EmailField()
    
