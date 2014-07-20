from django.shortcuts import render_to_response
from django.template import RequestContext

def profile(request): #Profile Page
    return render_to_response('accounts/profile.html', context_instance=RequestContext(request))

def edit_profile(request): #Edit Profile Page
    return render_to_response('accounts/edit_profile.html', context_instance=RequestContext(request))  