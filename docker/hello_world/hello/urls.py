
from django.conf.urls import url
from django.contrib import admin
from views import hello, quote

urlpatterns = [
    url(r'quote', quote),
    url(r'', hello),
]
