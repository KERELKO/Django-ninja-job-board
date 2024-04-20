from abc import abstractmethod

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

from src.apps.users.models import CustomUser
from src.apps.profiles.entities.profiles import (
    EmployerProfile as EmployerProfileEntity,
    JobSeekerProfile as JobSeekerProfileEntity,
    BaseProfile as BaseProfileEntity,
)


class BaseProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        related_name='%(class)s_related',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=250
    )
    last_name = models.CharField(
        max_length=250
    )
    email = models.CharField(
        max_length=60,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @abstractmethod
    def to_entity(self) -> BaseProfileEntity:
        ...


class JobSeekerProfile(BaseProfile):
    phone = models.CharField(
        max_length=25,
        blank=False,
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(limit_value=18),
            MaxValueValidator(limit_value=100),
        ]
    )
    about_me = models.TextField()
    experience = models.PositiveIntegerField(default=0)

    skills = ArrayField(
        models.CharField(max_length=30),
        blank=False,
    )

    class Meta:
        ordering = ('-first_name',)

    def save(self, *args, **kwargs):
        self.skills = [skill.lower() for skill in self.skills]
        return super().save(*args, **kwargs)

    def to_entity(self) -> JobSeekerProfileEntity:
        return JobSeekerProfileEntity(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            age=self.age,
            about_me=self.about_me,
            experience=self.experience,
            skills=self.skills,
            phone=self.phone,
        )


class EmployerProfile(BaseProfile):
    company_name = models.CharField(max_length=50)

    def to_entity(self) -> EmployerProfileEntity:
        return EmployerProfileEntity(
            id=self.id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            company_name=self.company_name,
        )