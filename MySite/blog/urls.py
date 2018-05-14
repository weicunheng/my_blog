from django.conf.urls import url
from . import views


# 把网址  和  业务处理函数 做一个关系映射
# name是处理函数index的别名
app_name='blog'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$',views.detail,name="detail"),
    url(r'^about/$',views.about,name="about")
]