try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from comments.views import Narrative

urlpatterns = patterns('',
    url(r'^$', Narrative.as_view(), name=Narrative.slug),
)