
from django import forms
class UsesDownloadWithYoutubelibrary(forms.Form):
    links = forms.CharField()
    #mail_address = forms.Charfield()
    def getNewurl():
        temp = getlinkdownloadNew(url)
        return temp
        file = forms.FileField()



        """class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)"""
