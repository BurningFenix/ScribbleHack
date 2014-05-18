from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

class UserProfile(UserenaBaseProfile):

    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    dob = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey(User)

