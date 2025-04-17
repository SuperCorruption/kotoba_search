from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from .views import home, search_articles, create_article, edit_article, view_article


app_name = 'articles'

urlpatterns = [
    path('', home, name='home'),
    path("search/", search_articles, name='search_articles'),
    path("create/", views.create_article, name="create_article"),
    path("edit/<str:work_title>/<str:title>/<str:author>/<int:article_id>", views.edit_article, name="edit_article_detailed"),
    path("article/<int:article_id>/", views.view_article, name="view_article"),
    path("article/<str:work_title>/<str:title>/<str:author>/<int:article_id>/", views.detailed_article_view, name="detailed_article_view"),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('permisson-denined/', views.permission_denied_view, name='permission_denied'),
]

