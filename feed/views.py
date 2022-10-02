from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import operator

from django.db.models import Q
from feed.models import Article


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context



class SearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get('search_box')
        if query:
            context['articles'] = Article.objects.filter(keywords__icontains=query)

        return context

class ArticleDetails(TemplateView):
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        article_id = self.request.path.split('/')
        print(article_id)
        article_id = article_id[-1]

        context = super(ArticleDetails, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get(id=article_id)
        return context
