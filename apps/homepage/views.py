from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login

def index(request): #Homepage
    return render_to_response('homepage/homepage.html', context_instance=RequestContext(request))

def login_user(request): #Login
	if(len(request.POST) > 0):
		user = request.POST['username']
		pw = request.POST['password']
		user = authenticate(username=user, password=pw)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render_to_response('profile.html', context_instance=RequestContext(request))
			else:
				print("user not active")
		else:
			print("user is none")
	return render_to_response('homepage/login.html', context_instance=RequestContext(request))

def abrowse(request): #Art Browse Page
    return render_to_response('homepage/art_browse.html', context_instance=RequestContext(request))

def wbrowse(request): #Writing Browse Page
    return render_to_response('homepage/writing_browse.html', context_instance=RequestContext(request))
