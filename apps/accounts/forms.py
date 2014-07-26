from django import forms
from django.utils.translation import ugettext as _

class EditProfileForm(forms.Form):
	age = forms.IntegerField(required=False)
	favorite_book = forms.CharField(label="Favorite Book",
		max_length=40, required=False)
	favorite_hero = forms.CharField(label="Favorite Hero",
		max_length=20, required=False)

	def clean(self):
		cleaned_data = super(EditProfileForm, self).clean()
		if cleaned_data['age'] is None \
			and cleaned_data['favorite_book'] == '' \
			and cleaned_data['favorite_hero'] == '':
			raise forms.ValidationError(
				_('No data given'), code='Null form')
		return cleaned_data

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=30, required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=True)
	password2 = forms.CharField(label='Type your password again',
		widget=forms.PasswordInput, required=True)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		pw1 = cleaned_data['password']
		pw2 = cleaned_data['password2']

		if pw1 and pw2 and pw1 != pw2:
			raise forms.ValidationError(
				_('Passwords are not the same'), code='Unequal passwords')
		return cleaned_data