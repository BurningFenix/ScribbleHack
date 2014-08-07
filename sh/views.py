from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
import random

# Homepage
class IndexView(TemplateView):
	template_name = 'homepage/homepage.html'

# will be removed in the future since art will become its own apps
############
class ArtBrowseView(TemplateView):
    template_name = 'homepage/art_browse.html'
############

# Picks a random 404 page
def custom404(request):
	template = '404error1.html'
	if random.random() > .5:
		template = '404error2.html'
	return render_to_response(template, context_instance=RequestContext(request))