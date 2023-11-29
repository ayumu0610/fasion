from django.urls import path
from . import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'blog-detail/<int:pk>/',
        views.BlogDetail.as_view(),
        name='blog_detail'
        ),
    #path('comment/<int:pk>/',views.CommentView.as_view(),name='comment'),
    path(
        'natural-list/',
        views.NaturalView.as_view(),
        name='natural_list'
        ),
    path(
        'beautiful-list/',
        views.BeautifulView.as_view(),
        name='beautiful_list'
        ),
    path(
        'casual-list/',
        views.CasualView.as_view(),
        name='casual_list'
        ),
    path(
        'cute-list/',
        views.CuteView.as_view(),
        name='cute_list'
        ),
    path(
        'cool-list/',
        views.CoolView.as_view(),
        name='cool_list'
        ),
    path(
        'mode-list/',
        views.ModeView.as_view(),
        name='mode_list'
        ),
    path(
        'contact/',
        views.ContactView.
        as_view(),
        name='contact'
    ),
]