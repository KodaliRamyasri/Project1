from django.db import models

# Create your models here.
class jobPost(models.Model):
    jobID=models.TextField(max_length=255)
    jobTitle=models.TextField(max_length=255)
    skills=models.TextField(max_length=255)
    experience=models.TextField(max_length=255)
    salary = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    def __str__(self):
        return self.jobTitle
    class Meta:
        db_table="addJobPost"