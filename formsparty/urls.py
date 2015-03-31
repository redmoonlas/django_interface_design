from django.conf.urls import patterns, url

from formsparty.views import Index, ContactWizard

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name=Index.slug),
    url(r'^wizard/$', ContactWizard.as_view(), name=ContactWizard.slug),
)