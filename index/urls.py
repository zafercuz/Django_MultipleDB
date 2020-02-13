from django.urls import path
from .views import IndexView, PostDetailView, PostCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/detail', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
]
