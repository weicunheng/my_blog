from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
import MyBlog.urls
import Comments.urls
import MessageBoard.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include(MyBlog.urls)),
    url(r'',include(Comments.urls)),
    url(r'',include(MessageBoard.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
