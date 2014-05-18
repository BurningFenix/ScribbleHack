from django import forms
from userena.forms import SignupForm
from django.forms import extras
from datetime import date

class SHForm(SignupForm):
    current_date = date.today()
    current_year = int(current_date.year) + 1
    dob = forms.DateField(widget=extras.SelectDateWidget(attrs={'class':'dropdown'}, years=range(1900, current_year)))

    def save(self):
        new_user = super(SHForm, self).save()
        new_user.dob = self.cleaned_data['dob']
        new_user.save()

        return new_user