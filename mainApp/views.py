from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoConversionForm
from .models import Video
from .tasks import ConversionAndSendingEmail
from django.conf import settings
#recipient = "fortestsonly23@gmail.com"
#subject = "Ссылка на скачивание Вашей песни"
#text = "Здесь должна быть ссылка на песню из медиа файла... сик оф зэсе факинг линкс"
#message = subject+text

def index(request):
    if request.method == "POST":
        form = VideoConversionForm(request.POST)

        if form.is_valid():
            link = form.cleaned_data['links']
            path, title = ConversionAndSendingEmail(link)
            email = form.cleaned_data['mail_address']
            send_mail(subject, text, settings.EMAIL_HOST_USER, [email])

            video = Video(email=email, path=path, title=title)
            video.save()

            return HttpResponse("<h1>Thank You. Your download link for {} is /get/{}.</h1> link will be sent to Your email".format(title, video.id))
    else:
        useForm = VideoConversionForm()
        return render (request,"mainApp/HomePage.html",{"form":useForm})


#def list(request):
    #return HttpResponse(list='title')


def download(request, filename):
    return HttpResponse(download='path')
