
from django.urls import path
from .views import PostListCreate, PostDetail, UserReigistration, CommentListCreate, CommentDetail

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('register/', UserReigistration.as_view(), name='user-registration'),
    path('posts/<int:post_id>/comments', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='commen-detail')
]
