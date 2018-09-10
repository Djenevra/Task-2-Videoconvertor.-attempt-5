from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
import os


app = Celery('review1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'review1.settings')
#settings.configure(default_settings=review1_defaults, DEBUG=True)
app.config_from_object('django.conf:settings', namespace='CELERY')




app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app = Celery('proj',
             broker='redis://',
             backend='redis://',
             include=['mainApp.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
