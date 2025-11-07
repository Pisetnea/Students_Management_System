# Create your views here.
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student


def student_management_system(request):
    return HttpResponse("Hello world!")

def find_student(request):
    return HttpResponse("Find Student Functionality")


def template_view(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def student_list(request):
  mystudent = Student.objects.all().values()
  template = loader.get_template('all_student.html')
  context = {
    'mystudent': mystudent,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
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