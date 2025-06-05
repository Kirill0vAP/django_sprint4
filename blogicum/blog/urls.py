from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # Главная страница и просмотр поста
    path('', views.index, name='index'),
    path('posts/<int:post_id>/',
         views.post_detail, name='post_detail'),
    # Категории
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts'),
    # Профиль пользователя
    path('profile/<str:username>/',
         views.profile, name='profile'),
    path(
        'profile/<str:username>/edit_profile/',
        views.profile_editing,
        name='edit_profile'),
    # CRUD для постов
    path('posts/create/',
         views.post_creating, name='create_post'),
    path('posts/<int:post_id>/edit/',
         views.post_editing, name='edit_post'),
    path('posts/<int:post_id>/delete/',
         views.post_deleting, name='delete_post'),
    # Комментарии
    path('posts/<int:post_id>/comment/',
         views.comment_adding, name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.comment_editing, name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.comment_deleting, name='delete_comment'),
]
