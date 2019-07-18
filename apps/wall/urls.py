from django.conf.urls import url   
from . import views 

urlpatterns = [
    url(r'^wall$', views.wall),
    url(r'^post_message$', views.postMessage),
    url(r'^post_comment$', views.postComment),
    url(r'^delete_message/(?P<id>\d+)$', views.deleteMessage),
    url(r'^delete_comment/(?P<id>\d+)$', views.deleteComment),
    url(r'^logout$', views.logout)
]
