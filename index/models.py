from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
