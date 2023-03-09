from django.urls import path
from .views import news_list, news_detail, HomePageView, contactPageView, _404PageView
urlpatterns = [
    path('', HomePageView, name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<int:id>/', news_detail, name='news_detail_page'),
    path('contact-us/', contactPageView, name='contact_page'),
    path('404/', _404PageView, name='404_page'),
]