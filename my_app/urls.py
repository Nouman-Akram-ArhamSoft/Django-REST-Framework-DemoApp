
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('student',views.StudentView)

urlpatterns = [
    path('', include(routers.urls))
]
