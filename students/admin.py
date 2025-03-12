from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','branch')






# from django.contrib import admin
# from .models import Auther, Book
# # Register your models here.

# @admin.register(Auther)
# class AutherAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email')
