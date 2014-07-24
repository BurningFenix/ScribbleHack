from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from apps.accounts.forms import EditProfileForm

@login_required(login_url='/accounts/login/')
def profile_view(request): #Profile Page
	age = request.user.age
	favorite_book = request.user.favorite_book
	favorite_hero = request.user.favorite_hero
	return render_to_response(
		'accounts/profile.html',
		{'age':age, 'favorite_book':favorite_book, 'favorite_hero':favorite_hero},
		context_instance=RequestContext(request)
	)

@login_required(login_url='/accounts/login/')
def edit_profile_view(request): #Edit Profile Pages
	if request.method == 'POST':
		form = EditProfileForm(request.POST)
		if form.is_valid():
			# works for the most part
			request.user.age = form.cleaned_data['age']
			request.user.favorite_book = form.cleaned_data['favorite_book']
			request.user.favorite_hero = form.cleaned_data['favorite_hero']
			request.user.save()
	else:
		form = EditProfileForm()
	return render_to_response('accounts/edit_profile.html', {'form': form}, context_instance=RequestContext(request))

def logout_view(request):
	# attepmts to log user out only if the user was already logged in
	if request.user.is_authenticated():
		logout(request)
	# probably should add something to show that the user was logged out successfully
	return render_to_response('homepage/homepage.html', context_instance=RequestContext(request))
