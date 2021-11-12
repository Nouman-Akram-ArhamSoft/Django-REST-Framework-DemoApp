from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_roll_no', 'student_name',
        'student_DOB', 'student_GPA',
        'student_address', 'student_phone_no',
        'student_section')
