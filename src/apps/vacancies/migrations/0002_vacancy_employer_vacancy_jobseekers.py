# Generated by Django 5.0.4 on 2024-04-14 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0003_alter_jobseekerprofile_options_and_more'),
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='employer',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='vacancies',
                to='profiles.employerprofile',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='jobseekers',
            field=models.ManyToManyField(
                blank=True,
                related_name='interested_in',
                to='profiles.jobseekerprofile',
            ),
        ),
    ]
