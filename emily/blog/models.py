from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField('published on')
    # created_by = models.ForeignKey('author', User)
    
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    # user = models.ForeignKey('author', User)
    # parent = models.ForeignKey(Comment)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField('posted at')
    
    def __unicode__(self):
        return self.title
        