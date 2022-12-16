from django.urls import path

from university_fbv import views

app_name = 'university_fbv'

urlpatterns = [
  path('', views.university_student_list, name='university_list'),
  path('university/new', views.university_create, name='university_new'),
  path('university/update/<int:pk>/', views.university_update, name='university_edit'),
  path('university/delete/<int:pk>/', views.university_delete, name='university_delete'),
  path('student/new/', views.student_create, name='student_create'),
  path('student/edit/<int:pk>/', views.student_update, name='student_edit'),
  path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),
]