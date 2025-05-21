"""
URL configuration for kotoba_search project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView
from articles import views
from articles.views import home, create_article, user_logout, search_articles, view_article, edit_article, delete_article, confirm_delete_article

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('article/<int:article_id>', view_article, name='view_article'),
    path('articles/', include(('articles.urls', 'articles'), namespace='articles')),
    path('', views.home, name='home'),
    path('search/', search_articles, name='search_articles'),
    path('logout/', user_logout, name='logout'),
    path('create/', create_article, name='create_article'),
    path("edit/<str:work_title>/<str:title>/<str:author>/<int:article_id>", views.edit_article, name="edit_article_detailed"),
    path("delete/<str:work_title>/<str:title>/<str:author>/<int:article_id>/confirm/", confirm_delete_article, name="confirm_delete_article"),
    path("delete/<int:article_id>/", views.delete_article, name="delete_article"),
    path('permisson_denied/', views.permission_denied_view, name='permission_denied'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

