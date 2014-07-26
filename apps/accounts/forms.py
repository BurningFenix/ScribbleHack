from django import forms
from django.utils.translation import ugettext as _

class EditProfileForm(forms.Form):
	age = forms.IntegerField(required=False)
	favorite_book = forms.CharField(label="Favorite Book",
		max_length=40, required=False)
	favorite_hero = forms.CharField(label="Favorite Hero",
		max_length=20, required=False)

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=30, required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=True)
	password2 = forms.CharField(label='Type your password again',
		widget=forms.PasswordInput, required=True)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		pw1 = cleaned_data.get('password')
		pw2 = cleaned_data.get('password2')

		if pw1 and pw2 and pw1 != pw2:
			raise forms.ValidationError(
				_('Passwords are not the same'), code='Unequal passwords')
		return cleaned_data