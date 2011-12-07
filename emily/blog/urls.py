from blog.forms import PostForm
from blog.models import Post
from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    # (Mostly) Restful URLs.
    url(r'^(?:posts/)*$', 'blog.views.post_index'),
    
    url(r'^posts/new*$', 
        ListView.as_view(
            queryset=PostForm(),
            context_object_name='form',
            template_name='posts/new.html'),
        name='post_new'),
        
    url(r'^posts/create/$', 'blog.views.post_create'),
            
    url(r'^post/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Post,
            template_name='posts/show.html')),
            
    url(r'^post/(?P<post_id>\d+)/edit/$', 'blog.views.post_edit'),            
    url(r'^post/(?P<post_id>\d+)/update/$', 'blog.views.post_update'),
    
    
    # URLs as specified by the project instructions.
    url(r'^(?P<slug>[^/]+)/$', 
        DetailView.as_view(
            model=Post,
            template_name='posts/show.html'),
        name='post_show_by_slug'),
)
