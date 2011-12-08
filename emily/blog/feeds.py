from django.contrib.comments import Comment
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404

from blog.models import Post


class RecentPostsFeed(Feed):
    title = 'Emily\'s Blog - Recent Posts'
    link = '/feeds/posts/recent'
    description = 'Our five most recent posts.'

    def items(self):
        return Post.objects.order_by('-created_at')[:5]
        
        
class AllPostsFeed(Feed):
    title = 'Emily\'s Blog - All Posts'
    link = '/feeds/posts/all'
    description = 'All of our posts.'

    def items(self):
        return Post.objects.order_by('-created_at')
       
        
class PostCommentsFeed(Feed):
    def get_object(self, request, pk):
        return get_object_or_404(Post, pk=pk)
        
    def get_object(self, request, slug):
        return get_object_or_404(Post, slug=slug)

    def title(self, obj):
        return 'Comments on %s' % obj.title

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        return Comment.objects.filter(content_type=Post, object_pk=obj.id).order_by('-submit_date')
        