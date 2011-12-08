from datetime import datetime

from django.views.generic.edit import CreateView

from blog.models import Comment, Post


class CreateCommentView(CreateView):
    model = Comment
    template_name = 'comments/new.html'

    def get_initial(self):
        # Get the initial dictionary from the superclass method.
        initial = super(CreateCommentView, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict.
        initial = initial.copy()
        
        # Set fields from request data.
        # Set the user to current user.
        # TODO: Make this a hidden field.
        initial['user'] = self.request.user.pk
        # Set the parent post to the post id provided in the parameters.
        # TODO: I can't get this to work correctly, either with the call to 
        # get the real object or just using the arg.  Both return the expected
        # id number, but I can't get the post to be pre-selected in the 
        # dropdown.
        # TODO: Make this a hidden field.  (Hopefully will also solve problem
        # mentioned in TODO above.)
        # initial['post'] = Post.objects.get(pk=self.kwargs.get('post')).id
        # Set the created_at time to now. 
        # TODO: Move this to a save method and remove the form field.
        initial['created_at'] = datetime.now
        return initial

