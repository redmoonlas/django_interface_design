try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from invaders.views import Intro

urlpatterns = patterns(
    '',
    url(r'^$', Intro.as_view(), name=Intro.slug),
)