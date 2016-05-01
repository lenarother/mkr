
from django.conf.urls import url
from django.contrib import admin
from views import hello

urlpatterns = [
    url(r'', hello)
]
