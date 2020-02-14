from django.urls import path
from .views import IndexView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/detail', PostDetailView.as_view(), name='detail'),
    path('create-post', PostCreateView.as_view(), name='create'),
    path('<int:pk>/update-post', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete-post', PostDeleteView.as_view(), name='delete'),
]
