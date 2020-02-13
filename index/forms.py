from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from index.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)
        widgets = {
            'content': SummernoteWidget(),
        }
