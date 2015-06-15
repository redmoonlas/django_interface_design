from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'', include('formsparty.urls', namespace='formsparty')),
    url(r'^cs/', include('coffescript.urls', namespace='coffescript')),
    url(r'^invaders/', include('invaders.urls', namespace='invaders')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^admin/', include(admin.site.urls)),
)
