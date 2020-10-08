from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class AllArticleApiView(APIView):
    def get(self, request, format=None):
        try:
            all_article = Article.objects.all()[:9]
            data = []
            for article in all_article:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url if article.cover else None,
                    'category': article.category.title,
                    'created_at': article.created_at,
                    'content': article.content,
                    'author': article.author.user.first_name,
                    'promote': article.promote,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

