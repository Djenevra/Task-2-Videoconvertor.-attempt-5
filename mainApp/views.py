from django.shortcuts import render
from django.http import HttpResponse
from .forms import videoconversionform
from .models import Video
from .tasks import videoconversion
from django.conf import settings
from django.core.mail import send_mail
#recipient = "fortestsonly23@gmail.com"
#subject = "Ссылка на скачивание Вашей песни"
#text = "Здесь должна быть ссылка на песню из медиа файла... сик оф зэсе факинг линкс"
#message = subject+text

def index(request):
    if request.method == "POST":
        form = videoconversionform(request.POST)

        if form.is_valid():
            link = form.cleaned_data['links']
            url, title = videoconversion(link)

            email = form.cleaned_data['mail_address']
            # send_mail(subject, text, settings.EMAIL_HOST_USER, [email])
            print(">>>> path ", url)
            video = Video(email=email, path=url, title=title)
            video.save()

            return HttpResponse("<h1>Thank You. Your download link for {} will be sent to Your email".format(title, video.id))
    else:
        useForm = videoconversionform()
        return render (request,"mainApp/HomePage.html",{"form":useForm})


#def list(request):
    #return HttpResponse(list='title')


def download(request, filename):
    return HttpResponse(download='path')
