from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from .models import Article
from .forms import SignUpForm

def home(request):
	return render(request, 'kusaco/home.html')

def testimonials(request):

	return render(request,'kusaco/testimonials.html')

def articles(request):
	art = Article.objects.order_by('-date_added')
	page = request.GET.get('page',1)

	paginator = Paginator(art, 1)

	try:
		art = paginator.page(page)
	except PageNotAnInteger:
		art = paginator.page(1)
	except EmptyPage:
		art = paginator.page(paginator.num_pages)



	
	context = {'art' : art}

	return render(request,'kusaco/articles.html',context)
	

def gallery(request):
	return render(request, 'kusaco/gallery.html')

def about(request):
	return render(request,'kusaco/about.html')

def events(request):
	return render(request,'kusaco/events.html')

def registration(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = username,password =raw_password)
			login(request,user)
			return redirect('login')

	else:
		form = SignUpForm()
	return render(request,'kusaco/registration.html', {'form': form})

