from django.shortcuts import redirect
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from .models import WritingPiece
from .forms import CreateWritingForm

class WritingListView(ListView):
	model = WritingPiece
	template_name = 'writing/browse_writing.html'#'writing/writing_list.html'
	# will show 20 writing pieces per page (5 rows)
	# pagination adds one query because it needs to know how many
	# WritingPiece entries exist in the database
	paginate_by = 20

	# gets one query set that follows the foreign key 'owner'
	def get_queryset(self):
		return self.model.objects.select_related('owner')

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

	# will only get the object if the user is the owner of the object
	def get_object(self):
		object = super(EditWritingView, self).get_object()

		# this will only allow you to get the object that
		# you are trying to edit if you are the owner
		# if you are not the owner, then no object is returned
		### currently uses another query to figure out who is the owner.
		### bonus points if can figure out how to make this more efficient
		if self.request.user == object.owner:
			return object
		else:
			return None

	def get(self, request, *args, **kwargs):
		response = super(EditWritingView, self).get(request, *args, **kwargs)
		if self.object is None:
			# if there is no object, then the user is not the owner
			# if the user is not the owner, then he/she is not
			# allowed to edit the object
			# this redirects them to the detail page
			return redirect('writing:detail', pk=kwargs['pk'])
		else:
			return response

class WritingDetailView(DetailView):
	model = WritingPiece
	template_name = 'writing/view_writing.html'