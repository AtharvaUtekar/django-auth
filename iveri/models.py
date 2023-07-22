from django.db import models
from users.models import NewUser  # Assuming you have a 'NewUser' model in the 'users' app

class PersonalDetails(models.Model):

    user = models.OneToOneField(NewUser, null=True, on_delete=models.CASCADE) 

    # email=user.email
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    adhaar_number = models.CharField(max_length=12, blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    # Other fields and their data types as required

    def __str__(self):
        return str(self.user)