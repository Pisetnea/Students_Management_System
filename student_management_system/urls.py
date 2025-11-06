from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('student_management_system/', views.student_management_system, name='student_management_system'),
    path('find_student/', views.find_student, name='find_student'),
    path('template_view/', views.template_view, name='template_view'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_list/detail/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
]

