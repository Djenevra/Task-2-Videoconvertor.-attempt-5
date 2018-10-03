from django.urls import include, re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    #re_path(r'^$', views.get_audiofile),

    #re_path(r'^list$', views.list),
    #re_path(r'^$', views.download)

    #re_path(r'^mainApp/convert/$',views.post),
]
