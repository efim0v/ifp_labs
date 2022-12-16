from sqlalchemy.ext.declarative import declarative_base
from wtforms_alchemy import ModelForm, ModelFieldList
from wtforms.fields import FormField

from django.contrib import admin
from university_fbv.models import University
from university_fbv.models import Student

admin.site.register(University)
admin.site.register(Student)