from django.contrib import admin
from django.urls import path, include
from . import views
#to upload image in db
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('messages', views.messages, name='messages')
]

#give permission to store the file in media folder
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)