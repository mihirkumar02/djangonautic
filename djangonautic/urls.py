from django.contrib import admin
from django.urls import path
from . import views # dot refers to same directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about),
    path('', views.home)
]
