from django import forms
from django.utils.translation import ugettext as _

class EditProfileForm(forms.Form):
	age = forms.IntegerField(required=False)
	favorite_book = forms.CharField(max_length=40, required=False)
	favorite_hero = forms.CharField(max_length=20, required=False)

	# modified the clean() removes all entries in dict that are None or ''
	# returns cleaned_data dict without any None or '' values
	def clean(self):
		cleaned_data = super(EditProfileForm, self).clean()
		if cleaned_data['age'] is None:
			del cleaned_data['age']
		if cleaned_data['favorite_book'] == '':
			del cleaned_data['favorite_book']
		if cleaned_data['favorite_hero'] == '':
			del cleaned_data['favorite_hero']
		if len(cleaned_data) == 0:
			raise forms.ValidationError(
				_('No data given'), code='Null form')
		return cleaned_data

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=30, required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=True)
	password2 = forms.CharField(widget=forms.PasswordInput, required=True)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		pw1 = cleaned_data['password']
		pw2 = cleaned_data['password2']

		# checks if the two passwords given are the same or not
		if pw1 and pw2 and pw1 != pw2:
			raise forms.ValidationError(
				_('Passwords are not the same'), code='Unequal passwords')
		return cleaned_data