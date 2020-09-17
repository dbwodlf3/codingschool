from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login.as_view(), name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^sign/$', views.signForm.as_view(), name='sign'),
]
