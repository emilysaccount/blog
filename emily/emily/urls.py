from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Admin functionalities.
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # Account management.
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', 
            name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', 
            {'next_page': '/'}, name='logout'),

    # Installed apps.
    url(r'^blog/', include('blog.urls')),
    url(r'', include('blog.urls')),
    
    # Django's comment framework.
    url(r'^comments/', include('django.contrib.comments.urls')),
)
