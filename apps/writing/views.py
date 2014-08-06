#from django.shortcuts import render
from django.views.generic import ListView, FormView
from braces.views import LoginRequiredMixin
from .models import WritingPiece
from .forms import CreateWritingForm


class WritingListView(ListView):
	model = WritingPiece
	template_name = 'writing/writing_list.html'

class CreateWritingView(LoginRequiredMixin, FormView):
	model = WritingPiece
	form_class = CreateWritingForm
	fields = ('name', 'content')
	template_name = 'writing/create_writing.html'
	success_url = '/writing/'

	def form_valid(self, form):
		WritingPiece(owner=self.request.user,
			name=form.cleaned_data['name'],
			content=form.cleaned_data['content'],
			allowed_contrib=form.cleaned_data['allowed_contrib']).save()
		
		return super(CreateWritingView, self).form_valid(form)
