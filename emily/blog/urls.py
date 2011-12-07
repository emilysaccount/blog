from blog.models import Post
from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Post URLs.
urlpatterns = patterns('',
    # (Mostly) Restful URLs.
    url(r'^(?:posts/)*$', 
        ListView.as_view(model=Post, template_name='posts/index.html', 
                         paginate_by=5),
        name='posts'),
        
    url(r'^posts/new/$', 
        CreateView.as_view(model=Post, template_name='posts/new.html'),
        name='new_post'),
            
    url(r'^post/(?P<pk>\d+)/$',
        DetailView.as_view(model=Post, template_name='posts/show.html'),
        name='post'),
            
    url(r'^post/(?P<pk>\d+)/edit/$', 
        UpdateView.as_view(model=Post, template_name='posts/edit.html'),
        name='edit_post'),            
    
    
    # URLs as specified by the project instructions.
    url(r'^(?P<slug>[^/]+)/$', 
        DetailView.as_view(model=Post, template_name='posts/show.html'),
        name='post_by_slug'),
)
