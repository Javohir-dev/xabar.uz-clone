from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import News, Category
from .forms import ContactForm


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


# def contactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Siz bilan tez orada bog'lanishadi.</h2>")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)
class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Siz bilan tez orada bog'lanishadi.</h2>")
        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)


def _404PageView(request):
    context = {}
    return render(request, 'news/404.html', context)
