from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm

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
			if form.cleaned_data['age'] is not None:
				request.user.age = form.cleaned_data['age']
			if form.cleaned_data['favorite_book'] != '':
				request.user.favorite_book = form.cleaned_data['favorite_book']
			if form.cleaned_data['favorite_hero'] != '':
				request.user.favorite_hero = form.cleaned_data['favorite_hero']
			request.user.save()
			return render_to_response('accounts/profile.html',
				context_instance=RequestContext(request))
	else:
		form = EditProfileForm({'age':request.user.age,
			'favorite_book':request.user.favorite_book,
			'favorite_hero':request.user.favorite_hero}
		)
		
	return render_to_response('accounts/edit_profile.html', {'form': form},
		context_instance=RequestContext(request))

def logout_view(request):
	# attepmts to log user out only if the user was already logged in
	if request.user.is_authenticated():
		logout(request)

	# probably should add something to show that
	# the user was logged out successfully
	return render_to_response('homepage/homepage.html',
		context_instance=RequestContext(request))
