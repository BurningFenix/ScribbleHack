from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .forms import EditProfileForm, RegisterForm
from .models import SHUser

from braces.views import LoginRequiredMixin

# when someone goes to /accounts/ it will automatically take you
# to either the login page or to your profile page
class IndexView(RedirectView):
	def get(self, request, *args, **kwargs):
		redirectPage = 'accounts:login'
		if request.user.is_authenticated():
			redirectPage = 'accounts:profile'
		return redirect(redirectPage)

# displays the profile page of the user currently logged in
class ProfileView(LoginRequiredMixin, DetailView):
	model = SHUser
	template_name = 'accounts/profile.html'

	# gets the object based on pk
	def get_object(self):
		# check if a pk value is given or if the request.user.pk
		# matches the one you are looking for. need to convert
		# self.request.user.pk into str to compare to self.kwargs['pk']
		# because it only holds string values
		if self.kwargs['pk'] is None \
			or self.kwargs['pk'] == str(self.request.user.pk):

			object = self.request.user
		else:
			try:
				object = self.model.objects.get(pk=self.kwargs['pk'])
			except:
				object = None
		return object

	# super gets the response, 404 if there is no object to display
	def get(self, request, *args, **kwargs):
		response = super(ProfileView, self).get(request, *args, **kwargs)
		if self.object is None:
			raise Http404
		else:
			return response


class EditProfileView(LoginRequiredMixin, FormView):
	template_name = 'accounts/edit_profile.html'
	form_class = EditProfileForm
	success_url = 'accounts:profile'

	def form_valid(self, form):
		changedUser = False
		# for everything that is valid (and not None/'')
		# itering through keys because the keys are also the
		# names of the attributes in the request.user instance
		for key in form.cleaned_data.keys():
			# not sure if should create var to store form.cleaned_data[key]
				
			# if not the same as stored value, set new value
			if form.cleaned_data[key] != getattr(self.request.user, key):
				setattr(self.request.user, key, form.cleaned_data[key])
				changedUser = True

		# only need to access the database if something was changed
		if changedUser == True:
			self.request.user.save()

		return redirect(self.success_url)

class LogoutView(RedirectView):
	url = '/'
	def get(self, request, *args, **kwargs):
		logout(request)
		# returns the redirect method RedirectView.get()
		return super(LogoutView, self).get(request, *args, **kwargs)

class RegisterView(FormView):
	template_name = 'accounts/register.html'
	form_class = RegisterForm
	success_url = 'accounts:profile'

	def form_valid(self, form):
		from .models import SHUser
		SHUser.objects.create_user(username=form.cleaned_data['username'],
			password=form.cleaned_data['password']).save()

		user = authenticate(username=form.cleaned_data['username'],
			password=form.cleaned_data['password'])
		login(self.request, user)
		return redirect(self.get_success_url())
