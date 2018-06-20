from django.conf.urls import url
from Comments import  views

app_name='comments'
urlpatterns = [
    url(r'^comments/blog/(?P<blog_pk>[0-9]+)/$',views.comments,name='comments')
]