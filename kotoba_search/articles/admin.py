from django.contrib import admin
from .models import Article
from django.contrib.auth.models import User
from django.contrib import messages
from users.utils import delete_authors_starting_with_a
# Register your models here.

@admin.action(description="Delete all articles")
def delete_all_articles(modeladmin, request, queryset):
    Article.objects.all().delete()
    messages.success(request, "All articles have been deleted.")

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    actions = [delete_all_articles, delete_authors_starting_with_a]

admin.site.register(Article, ArticleAdmin)
