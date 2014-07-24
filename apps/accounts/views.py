from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def profile(request): #Profile Page
    return render_to_response('accounts/profile.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def edit_profile(request): #Edit Profile Pages
	return render_to_response('accounts/edit_profile.html', context_instance=RequestContext(request))  