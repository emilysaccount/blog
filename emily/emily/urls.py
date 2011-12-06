from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Admin functionalities.
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Installed apps.
    url(r'^blog/', include('blog.urls')),
    url(r'', include('blog.urls'))
)
