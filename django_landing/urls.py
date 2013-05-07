from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

import settings

urlpatterns = patterns('',
     url(r'^$', include('landing.urls')),
     url(r'^/$', include('landing.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )