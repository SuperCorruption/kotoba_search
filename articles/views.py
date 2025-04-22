from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Article, Tag
from django.db.models import Q
from .forms import ArticleForm
from django.urls import reverse
import html

def kaigyou(text):
    escape = html.escape(text)
    return text.replace('\r\n', '<br>').replace('\n', '<br>').replace('\r', '<br>')

def Replace(title):
    escape = html.escape(title)
    return title.replace('_', ' ')

def home(request):
    latest_articles = Article.objects.order_by('-id')[:10]
    return render(request, 'articles/home.html', {'latest_articles':latest_articles})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect('home')

def permission_denied_view(request):
    return render(request, 'errors/permission_denied.html', status=403)

def search_articles(request):
    query = request.GET.get('q', '')
    tag_query = request.GET.get('tag', '')
    results = Article.objects.all()
    
    if query:
        keywords = query.strip().split()
        for word in keywords:
            results = results.filter(
                    Q(title__icontains=word) |
                    Q(work_title__icontains=word) |
                    Q(subtitle__icontains=word) |
                    Q(tags__name__icontains=word)
            ).distinct()

    if tag_query:
        results = results.filter(tags__name=tag_query)

    return render(request, 'articles/search.html', {'request': request, 'results': results, 'query': query, 'tag_query': tag_query,})

def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/article_detail.html', {'article': article})

def detailed_article_view(request, work_title, title, author, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_detail(request, work_title, title_slug, article_id):
    article = get_object_or_404(Article, pk=pk)
    if article.work_title != work_title or article.title_slug != title_slug:
        return redirect('article_detail', work_title=article.work_title, title_slug=article.title_slug, article_id=article_id)

    return render(request, 'article_detail.html', {'article': article})

def my_page(request, username):
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(author=user).order_by('-id')
    return render(request, 'articles/my_page.html', {'user': user, 'articles': articles})

@login_required
def create_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        content = kaigyou(content)
        work_title = request.POST.get('work_title')
        work_title = Replace(work_title)
        volume = request.POST.get('volume') or None
        episode = request.POST.get('episode') or None
        subtitle = request.POST.get('subtitle') or None
        page_number = request.POST.get('page_number') or None
        tags_input = request.POST.get('tags', '')

        author = request.user

        article = Article.objects.create(
                title=title,
                content=content,
                work_title=work_title,
                volume=volume,
                episode=episode,
                subtitle=subtitle,
                page_number=page_number,
                author=author
        )

        tag_names = [name.strip() for name in tags_input.split(',') if name.strip()]
        for name in tag_names:
            tag, _ =Tag.objects.get_or_create(name=name)
            article.tags.add(tag)

        return redirect(reverse('view_article', kwargs={
            'article_id': article.pk
        }))
    else:
        form = ArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})

@login_required
def edit_article(request, work_title, title, author, article_id):
    article = get_object_or_404(Article, id=article_id)

    if article.author != request.user:
        return redirect( 'permission_denied' )

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        content = kaigyou(content)
        work_title = request.POST.get('work_title')
        work_title = Replace(work_title)
        volume = request.POST.get('volume') or None
        episode = request.POST.get('episode') or None
        subtitle = request.POST.get('subtitle') or None
        page_number = request.POST.get('page_number') or None

        article.title = title
        article.content = content
        article.work_title = work_title
        article.volume = volume
        article.episode = episode
        article.subtitle = subtitle
        article.page_number = page_number

        tags_input = request.POST.get('tags', '')
        tag_names = [name.strip() for name in tags_input.split(',') if name.strip()]

        article.tags.clear()
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            article.tags.add(tag)

        article.save()
        return redirect("articles:detailed_article_view", work_title=article.work_title, title=article.title, author=article.author.username, article_id=article.id)

    else:
        form = ArticleForm(instance=article)
    tags_str = ', '.join(tag.name for tag in article.tags.all())
    return render(request, "articles/edit_article.html", {"form": form, "article": article, "tags": tags_str})
