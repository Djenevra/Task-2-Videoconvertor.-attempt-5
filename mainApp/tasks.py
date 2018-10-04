from __future__ import absolute_import, unicode_literals
from celery import shared_task
import smtplib
from .models import Video
import youtube_dl
from django.core.mail import send_mail
import json
#from review1 import settings



@shared_task
def videoconversion(currentLink):
    #path_template = 'media/uploads/%(title)s.%(ext)s'
    youtube_options = {
        'outtmpl': 'media/%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'audio-format': 'mp3',
        'extractaudio': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }
        ],
    }

    #path = None
    #id = None

    with youtube_dl.YoutubeDL(youtube_options) as youtubevariable:
        video_info = youtubevariable.extract_info(currentLink, download=True)
        id = video_info.get('id')

        #title = title.replace(" ", "")
    # file will be uploaded to MEDIA_ROOT/image/<filename>
        #ext = title.split('.')[-1]
        #title = "%s.%s" % (uuid.uuid4(), ext
    #'media/uploads/{0}'.format(filename)
        domain = 'http://127.0.0.1:8000/'
        format = '.mp3'
        path = 'mainApp/' + 'downloads/{}'.format(id)
        url = domain + path
        id = '{}'.format(id)
        print ("&&&&&", path)
        print (id)
        sender = "fortestsonly23@gmail.com"
        recipient = "fortestsonly23@gmail.com"
        subject = "Videoconvertor"
        text = "Click the link to download your mp3 file %s" % (url)
        message = "Subject: {}\n\n{}".format(subject, text)
        #send_mail(subject, message, sender, ['fortestsonly23@gmail.com'], fail_silently=False,)
        send_mail(subject, message, sender, ['fortestsonly23@gmail.com'])

    return url
