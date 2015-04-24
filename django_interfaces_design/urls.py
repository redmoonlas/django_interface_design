from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sites.models import Site

# current_site = Site.objects.get_current()
#
# if 'herokuapp' in current_site.domain:
#     urlpatterns = patterns('',
#         url(r'', include('formsparty.urls', namespace='formsparty')),
#         url(r'^adomino/', include(admin.site.urls)),
#     )
# else:

urlpatterns = patterns('',
    url(r'', include('formsparty.urls', namespace='formsparty')),
    url(r'^cs/', include('coffescript.urls', namespace='coffescript')),
    url(r'^invaders/', include('invaders.urls', namespace='invaders')),
    url(r'^admin/', include(admin.site.urls)),
)
