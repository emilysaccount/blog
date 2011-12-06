from blog.models import Post
from blog.models import Comment
from django.contrib import admin

##
# Classes to specify admin configuration.
##

# Setup for allowing Comments to be shown on the Post admin page.
class CommentInline(admin.StackedInline):
    model = Comment
    # We only want one comment form to be visible at a time.
    extra = 1

# Configure admin for the Post model.
class PostAdmin(admin.ModelAdmin):
    # Configuration for the list view.
    list_display = ('title', 'created_at')
    list_filter = ['created_at']
    # If this blog becomes large, we'll have to remove or optimize the 'body'
    # search so as to not overload the database.
    search_fields = ['question', 'body']
    date_hierarchy = 'created_at'
    
    # Configuration for the show/edit views.
    fields = ['title', 'slug', 'created_at', 'body']
    inlines = [CommentInline]

# Specify the order of fields for the Comment model.
class CommentAdmin(admin.ModelAdmin):
    fields = ['post', 'title', 'created_at', 'body']


##
# Register models with admin.
##

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
