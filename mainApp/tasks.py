from __future__ import absolute_import, unicode_literals
from celery import shared_task
import smtplib
from .models import Video
import youtube_dl
from django.core.mail import send_mail
import json
import re



@shared_task
def videoconversion(currentLink):
    #path_template = 'media/uploads/%(title)s.%(ext)s'
    youtube_options = {
        'outtmpl': 'media/uploads/%(title)s.%(ext)s',
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

    path = None
    title = None

    with youtube_dl.YoutubeDL(youtube_options) as youtubevariable:
        video_info = youtubevariable.extract_info(currentLink, download=True)
        title = video_info.get('title')




        #title = ' '.join(string.split())
        #title = re.sub(r'\s', '', title)

        domain = 'http://127.0.0.1:8000/'
        format = '.mp3'
        path = 'media/uploads/{}'.format(title)
        url = domain + path + format

    return url, title



#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#smtpObj.login('fortestsonly23@gmail.com','for123tests')


#sender = "fortestsonly23@gmail.com"
#recipient = "fortestsonly23@gmail.com"
#password = "for123tests"
#subject = "Videoconvertor"
#text = "Click the link to download your mp3 file %s" % (generated_path_to_mp3)
#path = [0]
#smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
#smtp_server.ehlo()
#smtp_server.starttls()
#smtp_server.login(sender,password)
#message = "Subject: {}\n\n{}".format(subject, text)
#smtp_server.sendmail(sender, recipient, message)
#smtp_server.quit()
