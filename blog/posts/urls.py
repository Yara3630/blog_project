from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'),
    path(
        'group/<slug:slug>/',
        views.group_list,
        name='group_list'),
    path(
        'create/',
        views.post_create,
        name='post_create'),
    path(
        'profile/<str:username>/',
        views.profile,
        name='profile'),
    path(
        'post/<int:post_id>/',
        views.post_detail,
        name='post_detail'),
    path(
        'post/<int:post_id>/edit/',
        views.post_edit,
        name='post_edit'),
    path(
        'post/<int:post_id>/comment_create/',
        views.create_comment,
        name='comment_create'),
    path(
        'profile/<str:username>/follow/',
        views.follow,
        name='follow'),
    path(
        'profile/<str:username>/unfollow/',
        views.unfollow,
        name='unfollow'),
    path(
        'favourite/',
        views.favourite,
        name='favourite'),
    path(
        'search/',
        views.SearchResultsView.as_view(),
        name='search_results'),
]
