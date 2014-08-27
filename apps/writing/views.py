from django.shortcuts import redirect
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from .models import WritingPiece
from .forms import CreateWritingForm

class WritingListView(ListView):
	model = WritingPiece
	template_name = 'writing/browse_writing.html'
	# will show 20 writing pieces per page (5 rows)
	# pagination adds one query because it needs to know how many
	# WritingPiece entries exist in the database
	paginate_by = 20

	# gets one query set that follows the foreign key 'author'
	def get_queryset(self):
		return self.model.objects.select_related('author')

class CreateWritingView(LoginRequiredMixin, FormView):
	model = WritingPiece
	form_class = CreateWritingForm
	fields = ('title', 'content')
	template_name = 'writing/create_writing.html'
	success_url = 'writing:index'

	def form_valid(self, form):
		WritingPiece(author=self.request.user,
			title=form.cleaned_data['title'],
			content=form.cleaned_data['content'],
			allowed_contrib=form.cleaned_data['allowed_contrib']).save()
		
		return redirect(self.success_url)

class EditWritingView(LoginRequiredMixin, UpdateView):
	model = WritingPiece
	fields = ['title', 'content']
	template_name = 'writing/edit_writing.html'
	
	def get_success_url(self):
		return reverse("writing:detail", kwargs={"pk":self.object.pk})

	# will only allow lookups of writingpiece that
	# the logged in user has created
	def get_queryset(self):
		return self.model.objects.filter(
			author=self.request.user
			).select_related('author')

	# will only get the object if the user is the author of the object
	def get_object(self):
		object = self.get_queryset().get(pk=self.kwargs['pk'])

		# this will only allow you to get the object that
		# you are trying to edit if you are the author
		# if you are not the author, then no object is returned
		### currently uses another query to figure out who is the author.
		### bonus points if can figure out how to make this more efficient
		###### used select_related() in queryset to make it more efficient
		if self.request.user == object.author:
			return object
		else:
			return None

	def get(self, request, *args, **kwargs):
		response = super(EditWritingView, self).get(request, *args, **kwargs)
		if self.object is None:
			# if there is no object, then the user is not the author
			# if the user is not the author, then he/she is not
			# allowed to edit the object
			# this redirects them to the detail page
			return redirect('writing:detail', pk=kwargs['pk'])
		else:
			return response

class WritingDetailView(DetailView):
	model = WritingPiece
	template_name = 'writing/view_writing.html'

	# gets one query set that follows the foreign key 'author'
	def get_queryset(self):
		return self.model.objects.select_related('author')