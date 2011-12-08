from django.conf.urls import patterns, url
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from blog.models import Comment, Post
from blog.views import CreateCommentView


# Post URLs.
urlpatterns = patterns('',
    # (Mostly) Restful URLs.
    url(r'^(?:posts/)*$', 
        ListView.as_view(model=Post, template_name='posts/index.html', 
                         paginate_by=5),
        name='posts'),
        
    url(r'^posts/new/$', 
        staff_member_required(CreateView.as_view(
                model=Post, 
                template_name='posts/new.html')),
        name='new_post'),
            
    url(r'^post/(?P<pk>\d+)/$',
        DetailView.as_view(model=Post, template_name='posts/show.html'),
        name='post'),
            
    url(r'^post/(?P<pk>\d+)/edit/$', 
        staff_member_required(UpdateView.as_view(
                model=Post, 
                template_name='posts/edit.html')),
        name='edit_post'),            
    
    
    # URLs as specified by the project instructions.
    url(r'^(?P<slug>[^/]+)/$', 
        DetailView.as_view(model=Post, template_name='posts/show.html'),
        name='post_by_slug'),
)

# Comment URLs.
urlpatterns += patterns('',
    url(r'^comments/new/$', 
        staff_member_required(CreateCommentView.as_view()),
        name='new_comment'),

    url(r'^comments/new/\?post_id=(?P<post>\d+)$', 
        staff_member_required(CreateCommentView.as_view()),
        name='new_comment_for_post'),
        
    url(r'^comment/(?P<pk>\d+)/edit/$', 
        staff_member_required(UpdateView.as_view(
                model=Comment, 
                template_name='comments/edit.html')),
        name='edit_comment'),
)
