from django import forms

class EditProfileForm(forms.Form):
	age = forms.IntegerField(required=False)
	favorite_book = forms.CharField(max_length=20, required=False)
	favorite_hero = forms.CharField(max_length=20, required=False)