from django import forms

class EditProfileForm(forms.Form):
	age = forms.IntegerField(required=False)
	favorite_book = forms.CharField(label="Favorite Book",
		max_length=40, required=False)
	favorite_hero = forms.CharField(label="Favorite Hero",
		max_length=20, required=False)