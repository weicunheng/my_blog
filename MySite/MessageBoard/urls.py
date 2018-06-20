from django.conf.urls import url
from MessageBoard import views

app_name='messageboard'
urlpatterns = [
    url(r'^message/$',views.message_board,name='message_board'),
    url(r'^message/(?P<page>[0-9]+)/$', views.message_board, name='message_board')
]