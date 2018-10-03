from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('downloads/<id>/', views.upload_file),
    #re_path(r'^$', views.get_audiofile),

    #re_path(r'^list$', views.list),
    #re_path(r'^$', views.download)

    #re_path(r'^mainApp/convert/$',views.post),
]
