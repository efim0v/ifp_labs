import datetime
from django.db import models
from django.urls import reverse

class University(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=100)
    creation_date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('university_fbv:university_edit', kwargs={'pk': self.pk})



class Student(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    middle_name = models.CharField(max_length=100, unique=True)
    birthday_date = models.DateField()
    university = models.ForeignKey(to='University', to_field='name', on_delete=models.PROTECT)
    enter_university_date = models.DateField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('university_fbv:university_edit', kwargs={'pk': self.pk})