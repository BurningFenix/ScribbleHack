from django.shortcuts import redirect, render
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
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
	success_url = 'writing:index'

	def form_valid(self, form):
		WritingPiece(owner=self.request.user,
			name=form.cleaned_data['name'],
			content=form.cleaned_data['content'],
			allowed_contrib=form.cleaned_data['allowed_contrib']).save()
		
		return redirect(self.success_url)

class EditWritingView(LoginRequiredMixin, UpdateView):
	model = WritingPiece
	fields = ['name', 'content']
	template_name = 'writing/edit_writing.html'
	
	def get_success_url(self):
		return reverse("writing:detail", kwargs={"pk":self.object.pk})

	def get_object(self):
		object = super(EditWritingView, self).get_object()

		# this will only allow you to get the object that
		# you are trying to edit if you are the owner
		# if you are not the owner, then no object is returned
		# (not sure what that error will look like)
		if self.request.user == object.owner:
			return object
		else:
			return None

class WritingDetailView(DetailView):
	model = WritingPiece
	template_name = 'writing/view_writing.html'