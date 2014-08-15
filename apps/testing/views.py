#from django.shortcuts import render
from django.views.generic import TemplateView

class BrowseWritingView(TemplateView):
	template_name = 'browse/browse_writing.html'

class HomepageView(TemplateView):
	template_name = 'homepage/homepage.html'

class EditProfileView(TemplateView):
	template_name = 'profile/editprofile.html'

class ProfileView(TemplateView):
	template_name = 'profile/profile.html'

class ProfileEditJournalView(TemplateView):
	template_name = 'profile/profile_edit_journal.html'

class SubmitView(TemplateView):
	template_name = 'submit/submit.html'

class DisplayWritingView(TemplateView):
	template_name = 'writing/displaywriting.html'
