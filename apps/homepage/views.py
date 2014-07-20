from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request): #Homepage
    return render_to_response('homepage/homepage.html', context_instance=RequestContext(request))

def login(request): #Login
    return render_to_response('homepage/login.html', context_instance=RequestContext(request))

def abrowse(request): #Art Browse Page
    return render_to_response('homepage/art_browse.html', context_instance=RequestContext(request))

def wbrowse(request): #Writing Browse Page
    return render_to_response('homepage/writing_browse.html', context_instance=RequestContext(request))