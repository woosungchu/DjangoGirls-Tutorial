from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import PostForm
from .models import Post
import json

@login_required
def post_list(request):
	login_user = request.user
	posts = Post.objects.filter(author=login_user, visible=True).order_by('-created_date')
	return render(request, 'blog/post_list.html',{'posts':posts})

@login_required
def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html',{'post':post})

@login_required
def post_new(request):
	if request.method == "POST" :
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else :
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_hide(request, pk):
	post = get_object_or_404(Post, pk=pk)
	client = request.user
	response_data = {'RESPONSE':'200'}
	
	if request.method == 'PUT' and request.is_ajax() and client==post.author :
		print(json)
		post.visible = False
		post.save()

		#response_data['HTTPRESPONSE'] = 200
	else :
		print('else')
		#response_data['HTTPRESPONSE'] = 500
		
		# All CODES above Works successfully 
		# but the code below.... 500 
	return HttpResponse(json.dumps(response_data),content_type="application/json")

   
   
   
   
   
   
   