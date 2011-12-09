from django.conf.urls import patterns, url
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from blog.feeds import RecentPostsFeed, AllPostsFeed, PostCommentsFeed
from blog.models import Post


# Post URLs.
urlpatterns = patterns('',
    # (Mostly) Restful URLs.
    url(r'^(?:posts/)*$', 
        ListView.as_view(model=Post, template_name='posts/index.html', 
                         paginate_by=10),
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


# Feed URLs.
urlpatterns += patterns('',
    url(r'^posts/recent/rss/$', RecentPostsFeed(), name='recent_posts_feed'),
    url(r'^posts/rss/$', AllPostsFeed(), name='all_posts_feed'),
    url(r'^post/(?P<pk>\d+)/rss/$', PostCommentsFeed(), 
        name='post_comments_feed'),
    url(r'^(?P<slug>[^/]+)/rss/$', PostCommentsFeed(),
        name='post_comments_feed_by_slug'),
)
