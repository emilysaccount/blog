from django.contrib import admin

from blog.models import Post


##
# Classes to specify admin configuration.
##

# Configure admin for the Post model.
class PostAdmin(admin.ModelAdmin):
    # Configuration for the list view.
    list_display = ('title', 'created_at')
    list_filter = ['created_at']
    # If this blog becomes large, we'll have to remove or optimize the 'body'
    # search so as to not overload the database.
    search_fields = ['title', 'body']
    date_hierarchy = 'created_at'
    
    # Configuration for the show/edit views.
    fields = ['title', 'slug', 'created_at', 'body']


##
# Register models with admin.
##

admin.site.register(Post, PostAdmin)
