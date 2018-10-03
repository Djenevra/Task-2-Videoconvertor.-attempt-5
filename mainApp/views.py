from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import videoconversionform
from .models import Video
from .tasks import videoconversion
from django.conf import settings
from django.core.mail import send_mail
import os
#recipient = "fortestsonly23@gmail.com"
#subject = "Ссылка на скачивание Вашей песни"
#text = "Здесь должна быть ссылка на песню из медиа файла... сик оф зэсе факинг линкс"
#message = subject+text

# http://127.0.0.1:8000/downloads/mwiQ0IKIlrk/

def index(request):
    if request.method == "POST":
        form = videoconversionform(request.POST)

        if form.is_valid():
            link = form.cleaned_data['links']
            url = videoconversion(link)

            email = form.cleaned_data['mail_address']
            #get_file = download(request, url)

            # send_mail(subject, text, settings.EMAIL_HOST_USER, [email])
            #print(">>>> path ", url)
            video = Video(email=email)
            video.save()


            print (url)

            url = download(request, id)

            #return HttpResponse("<h1>Thank You. Your download link will be sent to Your email</h1>")
    else:
        useForm = videoconversionform()
        return render (request,"mainApp/HomePage.html",{"form":useForm})


def download(request, id):

    id = format(id)
    url = os.path.join(settings.MEDIA_ROOT, format(id))
    #print url
    if os.path.exists(url):
        with open(url, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/mp3')
            response['Content-Disposition'] = 'attachment; filename = audio.mp3'

        return response






#def list(request):
    #return HttpResponse(list='title')


#def download(request, filename):
    #return HttpResponse(download='path')
