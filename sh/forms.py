from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import extras
from datetime import date

from userena.forms import SignupForm

attrs_dict = {'class': 'required'}

class SignupFormExtra(SignupForm):

    current_date = date.today()
    current_year = int(current_date.year) + 1
    dob = forms.DateField(widget=extras.SelectDateWidget(attrs={'class': 'dropdown'},
                                                         years=range(1900, current_year)),
                                                         required=True,
                                                         error_messages={'required': _('You must provide a date of birth.')})


    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={'required': _('You must agree to the terms to register.')})

    def save(self):
        """
        Override the save method to save the first and last name to the user
        field.
        """
        # First save the parent form and get the user.
        new_user = super(SignupFormExtra, self).save()
        new_user.dob = self.cleaned_data['dob']
        new_user.save()
        # Userena expects to get the new user from this form, so return the new
        # user.
        return new_user