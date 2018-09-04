
from django import forms


class VideoConversionForm(forms.Form):
    links = forms.CharField()
    mail_address = forms.EmailField()
    #file = forms.FileField()
    #def getNewurl():
        #temp = getlinkdownloadNew(url)
        #return temp
