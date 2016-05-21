from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
import json

#blog post
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = RichTextField()
	visible = models.BooleanField(default=True)
	created_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title

#color theme
#board category
class Symbol(models.Model):
    user = models.ForeignKey('auth.User')
#    font = models.CharField(max_length=100, default='Lobster')
    main_color = ColorField(default='#e6ccff')
    sub_color = ColorField(default='#ccff99')
    
    def __str__(self):
    	return self.user.__str__()
