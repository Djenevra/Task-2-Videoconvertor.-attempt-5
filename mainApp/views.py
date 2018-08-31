from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
import youtube_dl
from .forms import UsesDownloadWithYoutubelibrary
from .downloadsYoutube import getlinkdownloadNew

def index (request):
    if request.method == "POST":
        tempForm = UsesDownloadWithYoutubelibrary(request.POST)
        if tempForm.is_valid():
            temp2 = UsesDownloadWithYoutubelibrary()
            link = tempForm.cleaned_data['links']
            mail_address = tempForm.cleaned_data['mail_address']
            temp = getlinkdownloadNew(link)

            return redirect(temp)
    else:
        useForm = UsesDownloadWithYoutubelibrary()
        return render (request,"mainApp/HomePage.html",{"form":useForm})
