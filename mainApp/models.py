from django.db import models
#from uuid import UUID

#from django.db import IntegrityError

#def audio_path(filename):
    #ext = filename.split('.')[-1]
    #filename = "%s.%s" % (uuid.uuid4(), ext)
#return os.path.join('uploads/', filename)



class Video(models.Model):
    email = models.EmailField()
    #path = models.FileField (max_length=255, null=True, blank=True)
    #title = models.CharField(max_length=255)

    #def __str__(self):
        #return self.path






#class Pathes_to_converted_files(models.Model):

    # file will be uploaded to MEDIA_ROOT/uploads
    # upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    #upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
