from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from chatserver import views
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first, name='first'),
    path('enterroomnumber',views.enterroomnumber, name='enterroomnumber'),
    path('showchat',views.showchat,name='showchat'),

]
