from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, RegisterForm

#Profile Page
# might want to remove this decorator so that
# anonymous users can see profile pages
@login_required(login_url='/accounts/login/')
def profile_view(request):
	return render_to_response('accounts/profile.html',
		context_instance=RequestContext(request))

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

def logout_view(request):
	# attepmts to log user out only if the user was already logged in
	# also should figure out why logout() uses so many sql queries
	if request.user.is_authenticated():
		logout(request)

	# probably should add something to show that
	# the user was logged out successfully
	return redirect('/')

def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			# creates a new user using the create_user helper function
			from .models import SHUser
			SHUser.objects.create_user(form.cleaned_data['username'],
				password=form.cleaned_data['password']).save()

			# logs user in and redirects to profile page
			user = authenticate(username=form.cleaned_data['username'],
				password=form.cleaned_data['password'])
			login(request, user)
			return render_to_response('accounts/profile.html',
				context_instance=RequestContext(request))

	else:
		form = RegisterForm()
	return render_to_response('accounts/register.html', {'form': form},
		context_instance=RequestContext(request))
