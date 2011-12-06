from blog.models import Post
from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    # Restful URLs.
    url(r'^$', 'post_index'),
    url(r'^posts/$', 'post_index'),
    url(r'^post/(?P<post_id>\d+)/$', 'post_show'),
    url(r'^post/(?P<post_id>\d+)/edit/$', 'post_edit'),
    
    # URLs as specified by the project instructions.
    url(r'^(?P<slug>[^/]+)/$', 'post_show_by_slug'),
)
