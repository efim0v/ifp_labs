from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.forms import ModelChoiceField

from .models import University
from .models import Student

class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ['name', 'short_name', 'creation_date']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday_date', 'enter_university_date', 'university']


def university_student_list(request, template_name='university_fbv/university_student_list.html'):
    unibersity = University.objects.all()
    students = Student.objects.all()

    data = {}
    data['university_object_list'] = unibersity
    data['student_object_list'] = students


    return render(request, template_name, data)

def university_create(request, template_name='university_fbv/university_form.html'):
    form = UniversityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('university_fbv:university_list')
    return render(request, template_name, {'form':form})

def university_update(request, pk, template_name='university_fbv/university_form.html'):
    university = get_object_or_404(University, pk=pk)
    form = UniversityForm(request.POST or None, instance=university)
    if form.is_valid():
        form.save()
        return redirect('university_fbv:university_list')
    return render(request, template_name, {'form':form})

def university_delete(request, pk, template_name='university_fbv/delete_confirm.html'):
    university = get_object_or_404(University, pk=pk)    
    if request.method=='POST':
        university.delete()
        return redirect('university_fbv:university_list')
    return render(request, template_name, {'object':university})

def student_create(request, template_name='university_fbv/student_form.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('university_fbv:university_list')
    return render(request, template_name, {'form':form})

def student_update(request, pk, template_name='university_fbv/student_form.html'):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('university_fbv:university_list')
    return render(request, template_name, {'form':form})

def student_delete(request, pk, template_name='university_fbv/delete_confirm.html'):
    student = get_object_or_404(Student, pk=pk)    
    if request.method=='POST':
        student.delete()
        return redirect('university_fbv:university_list')
    return render(request, template_name, {'object':student})
