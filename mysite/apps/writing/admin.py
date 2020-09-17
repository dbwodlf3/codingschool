from django.contrib import admin
from writing.models import BoardPost, TestModel
# Register your models here.

class BoardPostAdmin(admin.ModelAdmin):
		readonly_fields = ['writedDate','alteredDate', 'writer', 'writer_nick_name', 'id']

admin.site.register(BoardPost, BoardPostAdmin)
admin.site.register(TestModel)