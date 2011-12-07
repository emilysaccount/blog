from blog.forms import PostForm
from blog.models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


# /posts
def post_index(request):
    # Get all Posts that have been written.
    post_list = Post.objects.all()
    
    # Setup a Paginator instance that will show 25 Posts at a time.
    paginator = Paginator(post_list, 25)

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_list = paginator.page(paginator.num_pages)

    return render_to_response('posts/index.html', {'post_list': post_list})
    
# /post/create
def post_create(request):
    # If this is a POST request, process the form.
    if request.method == 'POST': 
        form = PostForm(request.POST)
        if form.is_valid():
            # Create a new Post object from the data in the form.
            post = form.save()
            return HttpResponseRedirect(reverse('post_show_by_slug',
                                                args=(post.slug)))
                                                
        else: 
            return render_to_response('posts/new.html', {'form': form},
                                      context_instance=RequestContext(request))
        
    # If the user got to this page without a POST request, redirect them to
    # the index page.
    else:
        return HttpResponseRedirect(reverse('blog.views.post_index'))
    
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
                
            return HttpResponseRedirect(reverse('post_show_by_slug', 
                                                args=(post.slug)))
    # If the user somehow got to this page without using a POST request (which
    # shouldn't be happening with this URL design), send them back to the edit
    # page.
    else:
        return HttpResponseRedirect(reverse('blog.views.post_edit', 
                                            args=(post.id)))
    