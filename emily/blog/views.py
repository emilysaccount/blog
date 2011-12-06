from blog.forms import PostForm
from blog.models import Post

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


# /posts
def post_index(request):
    recent_posts = Post.objects.all().order_by('-created_at')[:5]
    return render_to_response('posts/index.html', 
                              {'recent_posts': recent_posts})
    
# /post/1   
def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('posts/show.html', {'post': post})
    
# /slug-1
def post_show_by_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('posts/show.html', {'post': post})
    
# /post/1/edit
def post_edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(instance=post)
    return render_to_response('posts/edit.html', {'post': post, 'form': form},
                              context_instance=RequestContext(request))

# /post/1/update
def post_update(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # TODO: Process the data in form.cleaned_data
        
            return HttpResponseRedirect(reverse('blog.views.post_show_by_slug', args=(post.slug,)))
        else:
            form = PostForm()

        return render_to_response('posts/edit.html', {'post': post, 
                                                      'form': form})
    