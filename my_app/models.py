from django.db import models

# Create your models here.
class Student(models.Model):
    student_roll_no = models.IntegerField(max_length=10, blank=False, null=False)
    student_name = models.CharField(max_length=100, blank=False, null=False)
    student_DOB = models.DateField()
    student_GPA = models.FloatField()
    student_address = models.TextField(null=True)
    student_phone_no = models.IntegerField(max_length=12)
    student_section = models.CharField(max_length=10, choices=[('A', "Section A"),
                                                ('B', "Section B"),
                                                ('C', "Section C")
                                                ])


    def __str__(self):
        return self.student_name
