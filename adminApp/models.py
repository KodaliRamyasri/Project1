from django.db import models

# Create your models here.
class contactUs(models.Model):
    firstName=models.TextField(max_length=255)
    lastName=models.TextField(max_length=255)
    email=models.EmailField(primary_key=True)
    comment=models.TextField(max_length=255)
    class Meta:
        db_table="contactUs"


