from django.db import models
from apps.account.models import BaseUser, GENDER_CHOICES, City


class Duration(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.name}"


class Technology(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    middle_name = models.CharField(max_length=225, blank=True, null=True)
    last_name = models.CharField(max_length=225, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    speciality = models.CharField(max_length=225, null=True, blank=True)
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE, null=True, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Organization(models.Model):
    description = models.TextField(null=True, blank=True)
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)


class Vacancy(models.Model):
    name = models.CharField(max_length=225)
    technologies = models.ManyToManyField(Technology, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    price = models.CharField(max_length=30, blank=True, null=True)
    vacancies = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name="organization_vacancies")
    link = models.CharField(max_length=225)
    
