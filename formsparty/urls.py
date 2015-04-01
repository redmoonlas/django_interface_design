from django.conf.urls import patterns, url

from formsparty.views import Index, ContactWizard, AuthorCreate, AuthorDetail, AuthorList

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name=Index.slug),
    url(r'^wizard/$', ContactWizard.as_view(), name=ContactWizard.slug),
    url(r'^author/$', AuthorList.as_view(), name=AuthorList.slug),
    url(r'^author/new$', AuthorCreate.as_view(), name=AuthorCreate.slug),
    url(r'^author/(?P<pk>\d+)/$', AuthorDetail.as_view(), name=AuthorDetail.slug),
)
