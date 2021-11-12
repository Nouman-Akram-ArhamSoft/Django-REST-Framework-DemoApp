from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response

from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Student
from rest_framework import viewsets, status, permissions
from rest_framework import serializers
from rest_framework import mixins
# Create your views here.

#
# class StudentView(APIView):
#
#     def get(self, request):
#         student_obj = Student.objects.all()
#         student_scr = StudentSerializer(student_obj, many=True)
#         return Response(student_scr.data)
#
#     def post(self, request):
#         student = StudentSerializer(data=request.data)
#         if student.is_valid():
#             student.save()
#             return Response(student)
#         else:
#             raise serializers.ValidationError('Invalid User')
#
#     def update(self, request):
#         pass
#
#     def delete(self, request):
#         pass



class StudentView(viewsets.ModelViewSet, mixins.DestroyModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
