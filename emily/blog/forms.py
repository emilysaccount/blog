from blog.models import Post, Comment
from django.forms import ModelForm

# Create a ModelForm class for Post.
class PostForm(ModelForm):
    class Meta:
        model = Post

# Create a ModelForm class for Comment.
class CommentForm(ModelForm):
    class Meta:
        model = Comment
