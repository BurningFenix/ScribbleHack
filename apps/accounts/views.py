from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from .forms import EditProfileForm, RegisterForm

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
class OwnProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'accounts/profile.html'

#Edit Profile Pages
@login_required(login_url='/accounts/login/')
def edit_profile_view(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST)
		if form.is_valid():
			changedUser = False
			# for everything that is valid (and not None/'')
			# itering through keys because the keys are also the
			# names of the attributes in the request.user instance
			for key in form.cleaned_data.keys():
				# not sure if should create var to store form.cleaned_data[key]
				
				# if not the same as stored value, set new value
				if form.cleaned_data[key] != getattr(request.user, key):
					setattr(request.user, key, form.cleaned_data[key])
					changedUser = True

			# only need to access the database if something was changed
			if changedUser == True:
				request.user.save()

			return render_to_response('accounts/profile.html',
				context_instance=RequestContext(request))
	else:
		# passing the dictionary will trigger validation of the form
		# use js or whatever if you want to provide hints
		form = EditProfileForm({'age':request.user.age,
			'favorite_book':request.user.favorite_book,
			'favorite_hero':request.user.favorite_hero}
		)

	return render_to_response('accounts/edit_profile.html', {'form': form},
		context_instance=RequestContext(request))

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

	# def get(self, request, *args, **kwargs):
	# 	form = RegisterForm()
	# 	return render_to_response('accounts/register.html', {'form':form})

	def form_valid(self, form):
		from .models import SHUser
		SHUser.objects.create_user(username=form.cleaned_data['username'],
			password=form.cleaned_data['password']).save()

		user = authenticate(username=form.cleaned_data['username'],
			password=form.cleaned_data['password'])
		login(self.request, user)
		return redirect(self.get_success_url())
