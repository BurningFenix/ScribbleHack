from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request): #Homepage
    return render_to_response('homepage/homepage.html', context_instance=RequestContext(request))

#def browse(request): #Forgot Password Page
    #return render_to_response('homepage/browse.html', context_instance=RequestContext(request))

#def congrats(request): #Forgot Password Page
    #return render_to_response('homepage/activation_complete.html', context_instance=RequestContext(request))