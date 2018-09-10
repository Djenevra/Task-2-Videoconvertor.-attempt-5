from __future__ import absolute_import, unicode_literals
from celery import shared_task
import smtplib
from .models import Video
import youtube_dl
from django.core.mail import send_mail
import json



@shared_task
def ConversionAndSendingEmail(currentLink):
    #path_template = 'media/uploads/%(title)s.%(ext)s'

    youtube_options = {
        'outtmpl': 'media/uploads/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        # 'audio-format': 'mp3',
        'extractaudio': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }
        ],
    }

    path = None
    title = None

    with youtube_dl.YoutubeDL(youtube_options) as youtubeVariable:
        video_info = youtubeVariable.extract_info(currentLink, download=True)
        title = video_info.get('title')
        ext = video_info.get('ext')



        #path = path_template % {'title': title, 'ext': ext}

    return path, title

path_template = 'media/uploads/%(title)s.%(ext)s'

generated_path_to_mp3 = '{domain}{path}{format}'.format(
            domain = 'http://127.0.0.1:8000',
            path = path_template, #% {'title': title, 'ext': ext},
            format='.mp3')
#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#smtpObj.login('fortestsonly23@gmail.com','for123tests')


#sender = "fortestsonly23@gmail.com"
#recipient = "fortestsonly23@gmail.com"
#password = "for123tests"
subject = "Videoconvertor"
text = "Click the link to download your mp3 file %s" % (generated_path_to_mp3)
path = [0]
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.ehlo()
smtp_server.starttls()
#smtp_server.login(sender,password)
message = "Subject: {}\n\n{}".format(subject, text)
#smtp_server.sendmail(sender, recipient, message)
smtp_server.quit()

@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
