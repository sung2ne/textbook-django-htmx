from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.get_posts, name='list'),
    path('create/', views.create_post, name='create'),
    path('<int:post_id>/', views.get_post, name='read'),
    path('<int:post_id>/update/', views.update_post, name='update'),
    path('<int:post_id>/delete/', views.delete_post, name='delete'),
    path('<int:post_id>/row/', views.get_post_row, name='row'),
    path('<int:post_id>/edit-row/', views.get_post_edit_row, name='edit-row'),
    path('<int:post_id>/save-row/', views.save_post_row, name='save-row'),
]
