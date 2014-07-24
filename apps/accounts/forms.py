from django import forms

class EditProfileForm(forms.Form):
	age = forms.IntegerField(required=False)
	favorite_book = forms.Charfield(max_length=20, required=False)
	favorite_hero = forms.Charfield(max_length=20, required=False)