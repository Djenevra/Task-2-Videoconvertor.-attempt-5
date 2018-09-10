from django.db import models


class Video(models.Model):
    email = models.EmailField()
    path = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.path






#class Pathes_to_converted_files(models.Model):

    # file will be uploaded to MEDIA_ROOT/uploads
    # upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    #upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
