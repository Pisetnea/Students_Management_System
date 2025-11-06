# from django.shortcuts import render

# Create your views here.
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student


def student_management_system(show):
    return HttpResponse("Hello world!")

def find_student(show):
    return HttpResponse("Find Student Functionality")


def template_view(show):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def student_list(specific):
  mystudents = Student.objects.all().values()
  template = loader.get_template('all_student.html')
  context = {
    'mystudents': mystudents,
  }
  return HttpResponse(template.render(context, specific))


def details(student, id):
  mystudent = Student.objects.get(id=id)
  template = loader.get_template('detail.html')
  context = {
    'mystudent': mystudent,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))