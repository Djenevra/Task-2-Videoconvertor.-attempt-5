from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    #re_path(r'^list$', views.list),
    #re_path(r'^download$', views.download)

    #re_path(r'^mainApp/convert/$',views.post),
]
