from django.conf.urls import patterns, url

from formsparty.views import Index

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name=Index.slug),
)