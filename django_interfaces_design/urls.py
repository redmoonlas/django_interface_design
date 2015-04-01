from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sites.models import get_current_site


if 'herokuapp' in get_current_site():
    urlpatterns = patterns('',
        url(r'', include('formsparty.urls', namespace='formsparty')),
        url(r'^adomin/', include(admin.site.urls)),
    )
else:
    urlpatterns = patterns('',
        url(r'', include('formsparty.urls', namespace='formsparty')),
        url(r'^admin/', include(admin.site.urls)),
    )
