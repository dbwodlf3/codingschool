from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BoardPost(models.Model):
	title = models.CharField(('Title Of Post'), max_length=100) #글의 제목 입니다.
	content = RichTextField(('Content Of Post')) #글의 내용 입니다.
	tag = models.CharField(max_length=10) #검색할 때 유용하게 쓸 수 있도록 태그를 작성 할 수 있게 합니다.

	#이곳에서부터는 사용자가 접근할 수 없는 메타 정보입니다.
	writedDate = models.DateTimeField(auto_now_add=True) #글이 쓰여진 날짜정보입니다. 따로 자겅할 필요는 없습니다.
	writer = models.CharField(max_length=30) #글의 작성자 id입니다. 따로 작성해야 합니다.#####
	writer_nick_name = models.CharField(max_length=15) # 글 작성자의 nick_name 입니다.
	boardTag = models.CharField(max_length=10) #게시판을 구분하기 위한 boardTag입니다. 사용자는 이 데이터를 직접적으로 수정할 수 없습니다. 따로 작성해야 합니다.####
	alteredDate = models.DateTimeField(auto_now=True) #글이 수정된 날짜입니다. 따로 작성하 필요는 없습니다.
	hits = models.IntegerField(default=0)#글의 조회수 입니다. 추후 추가해야합니다.####

	def __str__(self):
		return self.title

class TestModel(models.Model):
	dateTime = models.DateTimeField()
	dateTime_auto_now = models.DateTimeField(auto_now=True)
	dateTime_auto_now_add = models.DateTimeField(auto_now_add=True)
	helloWorld = models.DateTimeField()

class TestModel22(models.Model):
	dateTime = models.DateTimeField()
	dateTime_auto_now = models.DateTimeField(auto_now=True)
	dateTime_auto_now_add = models.DateTimeField(auto_now_add=True)
	helloWorld = models.DateTimeField()