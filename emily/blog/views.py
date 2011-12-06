from blog.models import Post
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

# /posts
def post_index(request):
    recent_posts = Post.objects.all().order_by('-created_at')[:5]
    return render_to_response('posts/index.html', {'recent_posts': recent_posts})
    
# /post/1   
def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('posts/show.html', {'post': post})
    
# /post/slug-1
def post_show_by_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('posts/show.html', {'post': post})
    