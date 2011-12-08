from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField('published on')
    # created_by = models.ForeignKey('author', User)
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('post_by_slug', [str(self.slug)])


class Comment(models.Model):
    post = models.ForeignKey(Post)
    # user = models.ForeignKey('author', User)
    # parent = models.ForeignKey(Comment)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField('posted at')
    
    def __unicode__(self):
        return self.title
        
    @models.permalink
    def get_absolute_url(self):
        # Yes, this is intentionally pointing to the show page for the post, 
        # not for this individual comment.  Comments don't have their own show
        # pages - we're not that fancy.  You read comments on the pages of 
        # their posts.
        # TODO: Figure out if there's a way to use self.post.get_absolute_url
        # here.  I haven't found a way that doesn't result in an error.
        return ('post', [str(self.post.id)])
        