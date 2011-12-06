from blog.forms import PostForm
from blog.models import Post

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

    
# /post/1/edit
def post_edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(instance=post)
    return render_to_response('posts/edit.html', {'post': post, 'form': form},
                              context_instance=RequestContext(request))

# /post/1/update
def post_update(request, post_id):
    # Get the appropriate Post.
    post = Post.objects.get(pk=post_id)
    
    # If this is a POST request, process the form.
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data.
            post.title = form.cleaned_data['title']
            post.slug = form.cleaned_data['slug']
            post.created_at = form.cleaned_data['created_at']
            post.body = form.cleaned_data['body']
            post.save()
                
            return HttpResponseRedirect(reverse('post_show_by_slug', args=(post.slug,)))
    # If the user somehow got to this page without using a POST request (which
    # shouldn't be happening with this URL design), send them back to the edit
    # page.
    else:
        return HttpResponseRedirect(reverse('blog.views.post_edit', args=(post.id,)))
    