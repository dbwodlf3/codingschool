from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main.as_view(), name='main'),
    url(r'^page/notice/$', views.notice.as_view(), name='notice'),
]