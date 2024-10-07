from django.shortcuts import render, get_object_or_404

from .models import Article

# Create your views here.
def index(request):
    articles_list = Article.objects.order_by('-created')
    context = {'articles_list': articles_list}
    return render(request, "blog/index.html", context)


def articles_list(request):
    articles = Article.published.all()
    return render(request, 'blog/list.html', {'articles': articles})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id, status=Article.Status.PUBLISHED)
    return render(request, 'blog/detail.html', {'article': article})