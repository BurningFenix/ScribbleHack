from django.shortcuts import render_to_response
from django.template import RequestContext
import random

def custom404(request):
	template = '404error1.html'
	if random.random() > .5:
		template = '404error2.html'
	return render_to_response(template, context_instance=RequestContext(request))