from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='Index'),
    url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
    url(r'^article/all/$', views.AllArticleApiView.as_view(), name='article'),
]
