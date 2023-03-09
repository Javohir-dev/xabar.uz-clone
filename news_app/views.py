from django.shortcuts import render, get_object_or_404
from .models import News, Category


def news_list(request):
    # news_list = News.published.filter(status=News.Status.Published)
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context=context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        "news": news,
    }
    return render(request, "news/news_detail.html", context=context)


def HomePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'category': categories,
    }
    return render(request, 'news/home.html', context)


def contactPageView(request):
    context = {}
    return render(request, 'news/contact.html', context)


def _404PageView(request):
    context = {}
    return render(request, 'news/404.html', context)
