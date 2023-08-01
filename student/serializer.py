from rest_framework import  serializers
from django.utils.translation import gettext_lazy as _
from .models import (
    Student,
 
) 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

