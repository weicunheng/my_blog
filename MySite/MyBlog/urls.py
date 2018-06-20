from django.conf.urls import url
from MyBlog import views

app_name='blog'
urlpatterns = [
    url(r'^$',views.index,),
    url(r'^index/$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^blog/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^tag/(?P<tag>\w+)$', views.tag, name='tag'),
    url(r'^search/$', views.search, name='search'),
    url(r'^archives/$', views.archives_html, name='archives_html'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<title>\w+)/$',views.category,name='category'),
    url(r'^source/$',views.source,name='source'),
]