from collections import namedtuple

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import connections
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
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


class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create-update.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['card_header'] = "Create Post"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super(PostCreateView, self).form_valid(form)
        messages.success(self.request, "Post successfully created!")
        return response


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'create-update.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['card_header'] = "Update Post"
        context['update'] = 1
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super(PostUpdateView, self).form_valid(form)
        messages.success(self.request, "Post successfully updated!")
        return response

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('index')
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['card_header'] = "Delete Post"
        return context

    def delete(self, request, *args, **kwargs):
        response = super(PostDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, "Post successfully deleted!")
        return response

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
