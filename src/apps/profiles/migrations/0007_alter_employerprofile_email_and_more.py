# Generated by Django 5.0.4 on 2024-04-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0006_jobseekerprofile_allow_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerprofile',
            name='email',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='email',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
