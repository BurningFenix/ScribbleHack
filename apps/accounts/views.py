from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .forms import EditProfileForm, RegisterForm
from .models import SHUser

from braces.views import LoginRequiredMixin

class OtherProfileView(DetailView):
	model = SHUser
	template_name = 'accounts/profile.html'

# when someone goes to /accounts/ it will automatically take you
# to either the login page or to your profile page
class IndexView(RedirectView):
	def get(self, request, *args, **kwargs):
		redirectPage = 'accounts:login'
		if request.user.is_authenticated():
			redirectPage = 'accounts:profile'
		return redirect(redirectPage)

# displays the profile page of the user currently logged in
class OwnProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'accounts/profile.html'

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
