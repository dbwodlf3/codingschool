from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

class main(View):
	template_name='index.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)