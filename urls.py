from django.conf.urls import patterns, include, url
from django.contrib import admin

from octo_cv.views import HomeView, ContactView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact/', ContactView.as_view(), name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
