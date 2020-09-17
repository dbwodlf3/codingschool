from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .forms import BoardForm
from writing.models import BoardPost
from django.urls import reverse
import math
# Create your views here.

class write(View):
	template_name ='writing/write.html'
	form = 	BoardForm()
	context = {'form': form}
	def get(self, request, *args, **kwargs):
		my_user = request.user.is_authenticated
		if my_user:
			return render(request, self.template_name, self.context)
		else:
			return HttpResponse('로그인 해 주세요.')
		#return HttpResponse(self.template_name)

	def post(self, request, *args, **kwargs):
		title = str(request.POST['title'])
		content = request.POST['content']
		tag  = request.POST['tag']
		boardTag = request.POST['boardTag']
		writer = request.user.username
		writer_nick_name = request.user.nick_name

		userBoardPost = BoardPost.objects.create()
		userBoardPost.title = title
		userBoardPost.content = content
		userBoardPost.tag = tag
		userBoardPost.boardTag = boardTag
		userBoardPost.writer= writer
		userBoardPost.writer_nick_name = writer_nick_name
		userBoardPost.save()
		return HttpResponseRedirect('/writing/board/free/1')
#		output = writer_nick_name
#		return HttpResponse(output)

class read(View):
	template_name = 'writing/read.html'
	context = {}
	def get(self, request, *args, **kwargs):
		userBoardPost = BoardPost.objects.get(boardTag = kwargs['board'], id = kwargs['id'])
		self.context['BoardPost'] = userBoardPost

		try:
			request.session[str(BoardPost.id)]
		except KeyError:
			request.session[str(BoardPost.id)] = True
			userBoardPost.hits += 1
			userBoardPost.save()

		return render(request, self.template_name, self.context)
		#return HttpResponse(userBoardPost.content)

class board(View):
	template_name = 'writing/board.html'
	context = {}

	def get(self, request, *args, **kwargs):
		## 파라미터를 받아와 기본적인 상수를 변수에 저장합니다.
		pageNumber = int(kwargs['page']) # 페이지의 넘버를 저장합니다.
		userBoardPost = BoardPost.objects.all().defer('content').order_by('-id') # 게시판에 있는 모든 게시글을 역순으로 받습니다.
		itemLength = userBoardPost.count() # 게시판에 있는 모든 게시물의 개수를 샙니다.
		pageView = 16

		pageLength = math.ceil( itemLength / pageView ) ## 나타낼 수 있는 총 페이지수를 정합니다.
		pageLengthRemainder = itemLength-pageLength*pageView ## 나타낼 수 있는 총 페에지수 마지막 페이지의 표시할 것들을 나타냅니다. 나머지입니다.
		
		startBoard = (pageNumber-1)*pageView
		endBoard =pageNumber*pageView
		userBoardPost = userBoardPost[startBoard:endBoard] ##페이지에 나타낼 게시글들을 반환합니다. 이걸로 완벽!

		self.context['BoardPost'] = userBoardPost
		self.context['pageNumber'] = pageNumber
		self.context['pageCount'] = pageLength
		self.context['Board'] = kwargs['board']
		return render(request, self.template_name, self.context)

def pageControl(request, *args, **kwargs):
	boardName=request.POST['Board']
	pageNumber=request.POST['pageNumber']
	return HttpResponseRedirect(reverse('writing:board', args=[boardName, pageNumber]))

class delete(View):
	def get(self, request, *args, **kwargs):
		return HttpResponseRedirect('/')

	def post(self, request, *args, **kwargs):
		BoardPostBoardTag = request.POST['BoardPostBoardTag']
		BoardPostId = request.POST['BoardPostId']
		userBoardPost = BoardPost.objects.get(boardTag = BoardPostBoardTag, id = BoardPostId)
		userBoardPost.delete()
		return HttpResponseRedirect('/writing/board/free/1')
