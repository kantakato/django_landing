from django.conf.urls import patterns, include, url
from landing.views import LandingCreateView

urlpatterns = patterns('',
                       url(r'^$', LandingCreateView.as_view(), name = "landing"),
                       )