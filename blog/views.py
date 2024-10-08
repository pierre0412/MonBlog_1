from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article

# Create your views here.
def index(request):
    article_list = Article.objects.order_by('-created')
    context = {'article_list': article_list}
    return render(request, "blog/index.html", context)


def articles_list(request):
    articles = Article.published.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page', 1)
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        #If page_number is not an integer get the first page
        articles = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'articles': articles})


def article_detail(request, year, month, day, article):
    article = get_object_or_404(Article,
                                status=Article.Status.PUBLISHED,
                                slug=article,
                                created__year=year,
                                created__month=month,
                                created__day=day,
                                )
    return render(request, 'blog/detail.html', {'article': article})