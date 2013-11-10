from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from settings import MEDIA_URL, MEDIA_ROOT
from octo_cv.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact/', ContactView.as_view(), name='contact'),
    url(r'^education/', EducationView.as_view(), name='education'),
    url(r'^work/', WorkView.as_view(), name='work'),
    url(r'^volunteer/', VolunteerView.as_view(), name='volunteer'),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
