# Generated by Django 5.0.4 on 2024-04-14 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_rename_jobseekers_vacancy_interested'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='interested',
            new_name='interested_candidates',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='remote',
            new_name='is_remote',
        ),
    ]
