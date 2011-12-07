from blog.forms import PostForm
from blog.models import Post

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.create_update import create_object
from django.views.generic.list_detail import object_list


# /posts
def post_index(request):
    return object_list(request, queryset=Post.objects.all(),
                       template_object_name='post',
                       template_name='posts/index.html',
                       paginate_by=5)
    
# /post/create
@login_required
def post_create(request):
    return create_object(request, form_class=PostForm, 
                         template_name='posts/new.html', login_required=True)
    
# /post/1/edit
@login_required
def post_edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(instance=post)
    return render_to_response('posts/edit.html', {'post': post, 'form': form},
                              context_instance=RequestContext(request))

# /post/1/update
@login_required
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
                
            return HttpResponseRedirect(reverse('post_show_by_slug', 
                                                args=(post.slug)))
    # If the user somehow got to this page without using a POST request (which
    # shouldn't be happening with this URL design), send them back to the edit
    # page.
    else:
        return HttpResponseRedirect(reverse('blog.views.post_edit', 
                                            args=(post.id)))
    