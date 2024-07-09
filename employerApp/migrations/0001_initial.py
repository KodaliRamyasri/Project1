# Generated by Django 5.0.6 on 2024-06-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobID', models.TextField(max_length=255, unique=True)),
                ('jobTitle', models.TextField(max_length=255)),
                ('skills', models.TextField(max_length=255)),
                ('experience', models.TextField(max_length=255)),
                ('salary', models.TextField(max_length=255)),
                ('location', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'addJobPost',
            },
        ),
    ]
