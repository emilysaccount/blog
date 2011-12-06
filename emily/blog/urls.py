from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'post_index'),
    url(r'^posts/$', 'post_index'),
    url(r'^post/(?P<post_id>\d+)/$', 'post_show'),
    url(r'^post/(?P<post_id>\d+)/edit/$', 'post_edit'),
)