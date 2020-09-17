from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class main(View):
	template_name='page/index.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class notice(View):
	template_name='page/notice.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		return HttpResponseRedirect('/')