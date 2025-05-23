from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from .views import home, search_articles, create_article, edit_article, view_article, delete_article, confirm_delete_article

app_name = 'articles'

urlpatterns = [
    path('', home, name='home'),
    path("search/", search_articles, name='search_articles'),
    path("create/", views.create_article, name="create_article"),
    path("edit/<str:work_title>/<str:title>/<str:author>/<int:article_id>", views.edit_article, name="edit_article_detailed"),
    path("delete/<int:article_id>/confirm/", confirm_delete_article, name="confirm_delete_article"),
    path("delete/<int:article_id>/", views.delete_article, name="delete_article"),
    path("article/<int:article_id>/", views.view_article, name="view_article"),
    path("article/<str:work_title>/<str:title>/<str:author>/<int:article_id>/", views.detailed_article_view, name="detailed_article_view"),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('permission_denied/', views.permission_denied_view, name='permission_denied'),
    path('mypage/<str:username>/', views.my_page, name='my_page'),
]

