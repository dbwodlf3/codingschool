from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BoardPost

class BoardForm(forms.ModelForm):
	CHOICES = {
			('free', 'free')
		}
	title = forms.CharField(required=True)
	content = forms.CharField(widget=CKEditorWidget())
	tag = forms.CharField(required=True)
	boardTag = forms.ChoiceField(choices=CHOICES, required=True, label='BoardTag')

	class Meta:
		model = BoardPost
		fields = ('title', 'content', 'tag')