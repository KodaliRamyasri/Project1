# Generated by Django 5.0.6 on 2024-06-25 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employerApp', '0002_alter_jobpost_jobid'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('coverLetter', models.TextField()),
                ('jobDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employerApp.jobpost')),
            ],
        ),
    ]