# Generated by Django 5.0.4 on 2024-04-13 12:18

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobSeekerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=25)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(limit_value=12), django.core.validators.MaxValueValidator(limit_value=100)])),
                ('about_me', models.TextField()),
                ('experience', models.PositiveIntegerField(default=0)),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
            ],
            options={
                'ordering': ('experience',),
            },
        ),
    ]
