from django.shortcuts import render

from blog.models import Article


# Create your views here.
def index(request):
    articles_list = Article.objects.order_by('-created')
    context = {'articles_list': articles_list}
    return render(request, "blog/index.html", context)
