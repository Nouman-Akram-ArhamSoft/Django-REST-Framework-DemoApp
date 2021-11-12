from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    def validate_student_GPA(self, value):
        if value < 0 or value > 4:
            raise serializers.ValidationError()
        else:
            return value