from django.conf.urls import *

urlpatterns = patterns('multilingual.flatpages.views',
    (r'^(?P<url>.*)$', 'multilingual_flatpage'),
)
