from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'write/$', views.write.as_view(), name='write'),
	url(r'read/(?P<board>.+)/(?P<id>[0-9]+)/$', views.read.as_view(), name = 'read'),
	url(r'board/(?P<board>.+)/(?P<page>[0-9]+)/$', views.board.as_view(), name='board'),
	url(r'pageControl/$', views.pageControl, name='pageControl'),
	url(r'delete/$', views.delete.as_view(), name='delete'),
]