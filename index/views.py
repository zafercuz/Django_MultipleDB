from collections import namedtuple

from django.contrib.auth.models import User
from django.db import connections
from django.views.generic import ListView

from .models import Post
from mysql_models.models import IndexProduct, IndexImage


def namedtuplefetchall(cursor):
    """Return all rows from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.all()
        return posts

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        """ ORM query style """
        posts_mysql = IndexImage.objects.using('mdb_mysql').all()
        product_mysql = IndexProduct.objects.using('mdb_mysql').all()

        """ Raw query style """
        with connections['mdb_mysql'].cursor() as cursor:
            cursor.execute("SELECT * from index_product_category")
            row = namedtuplefetchall(cursor)

        print(row)
        context['title'] = 'Multiple Database'
        context['posts_mysql'] = posts_mysql
        context['product_mysql'] = product_mysql
        context['product_category_mysql'] = row
        return context
