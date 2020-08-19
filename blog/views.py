from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class IndexPage(TemplateView):

    def get(self, request, **kwargs):

        article_data = []
        all_articles = Article.objects.all()[:9]
        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at,

            })

        promote_data = []
        all_promote_article = Article.objects.filter(promote=True)
        for promote_article in all_promote_article:
            promote_data.append({
                'title': promote_article.title,
                'cover': promote_article.cover.url,
                'category': promote_article.category.title,
                'author': promote_article.author.user.first_name,
                'avatar': promote_article.author.avatar.url if promote_article.author.avatar else None,
                'created_at': promote_article.created_at,

            })

        context = {
            'article_data': article_data,
            'promote_data_article': promote_data,
        }

        return render(request, 'index.html', context)


class ContactPage(TemplateView):
    template_name = "page-contact.html"

