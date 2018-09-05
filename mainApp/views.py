from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoConversionForm
from .models import Video
from .downloadsYoutube import getlinkdownloadNew


def index(request):
    if request.method == "POST":
        form = VideoConversionForm(request.POST)

        if form.is_valid():
            link = form.cleaned_data['links']
            path, title = getlinkdownloadNew(link)
            email = form.cleaned_data['mail_address']

            video = Video(email=email, path=path, title=title)
            video.save()

            return HttpResponse("<h1>Thank You. Your download link for {} is /get/{}.</h1>".format(title, video.id))
    else:
        useForm = VideoConversionForm()
        return render (request,"mainApp/HomePage.html",{"form":useForm})


def list(request):
    return HttpResponse(list='title')


def download(request, filename):
    return HttpResponse(download='path')
