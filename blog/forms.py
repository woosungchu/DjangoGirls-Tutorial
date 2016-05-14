from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta: #tell to django which model should be target 
		model = Post
		fields=('title', 'text',)
