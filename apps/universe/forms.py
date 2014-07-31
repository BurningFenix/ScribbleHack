from django import forms

class CreateWritingForm(forms.Form):
	name = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)
	allowed_contrib = forms.BooleanField(required=False)
