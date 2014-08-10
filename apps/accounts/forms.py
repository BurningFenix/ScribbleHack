from django import forms
from django.utils.translation import ugettext as _

class EditProfileForm(forms.Form):
	books = forms.CharField(required=False)
	artworks = forms.CharField(required=False)
	artists = forms.CharField(required=False)
	tv_movies = forms.CharField(required=False)
	music = forms.CharField(required=False)
	videogames = forms.CharField(required=False)

	# modified the clean() removes all
	# entries in dict that are None or ''
	# returns cleaned_data dict without any None or '' values
	def clean(self):
		cleaned_data = super(EditProfileForm, self).clean()
		# since everything is a char/text field, empty values will
		# always be '', this is to make the dict smaller where possible
		for key in cleaned_data.keys():
			if cleaned_data[key] == '':
				del cleaned_data[key]

		# if all values are empty
		if len(cleaned_data) == 0:
			raise forms.ValidationError(
				_('No data given'), code='Null form')
		return cleaned_data

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=30, required=True)
	password = forms.CharField(required=True)
	password2 = forms.CharField(required=True)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		pw1 = cleaned_data['password']
		pw2 = cleaned_data['password2']

		# checks if the two passwords given are the same or not
		if pw1 and pw2 and pw1 != pw2:
			raise forms.ValidationError(
				_('Passwords are not the same'),
				code='Unequal passwords')
		return cleaned_data