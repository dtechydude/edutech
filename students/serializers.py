from rest_framework import serializers
from . models import StudentDetail

class StudentDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentDetail
        fields = '__all__'