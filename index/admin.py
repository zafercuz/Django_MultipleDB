from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content',)
    fields = ('title', 'content', )
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
