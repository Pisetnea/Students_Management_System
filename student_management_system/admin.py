from django.contrib import admin

# Register your models here.
from .models import Student

# Register your models here.
# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date", "email", "phone")

admin.site.register(Student, StudentAdmin)