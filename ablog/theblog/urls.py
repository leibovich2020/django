from django.urls import path
# from . import views
from .views import HomeView, ArticleDetaliView, AddPostView, UpdatePostView ,DeletPostView,LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name = "home"),
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', ArticleDetaliView.as_view(), name = 'article-detail'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('article/<int:pk>/remove', DeletPostView.as_view(), name = 'delete_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]