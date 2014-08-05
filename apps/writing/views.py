#from django.shortcuts import render
from django.views.generic import ListView, FormView
from braces.views import LoginRequiredMixin
from .models import Writing
from .forms import CreateWritingForm


class WritingListView(ListView):
	model = Writing

class CreateWritingView(LoginRequiredMixin, FormView):
	model = Writing
	form_class = CreateWritingForm
	fields = ('name', 'content')
	template_name = 'universe/create_writing.html'
	success_url = '/universe/writing/'

	def form_valid(self, form):
		Writing(owner=self.request.user,
			name=form.cleaned_data['name'],
			content=form.cleaned_data['content'],
			allowed_contrib=form.cleaned_data['allowed_contrib']).save()
		
		return super(CreateWritingView, self).form_valid(form)
