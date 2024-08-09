from rest_framework import serializers
from students.models import StudentDetail

class StudentDetailSerializer(serializers.ModelSerializer):
        student = serializers.SlugRelatedField(
        slug_field='student_username',
        queryset=StudentDetail.objects.all()
    )
    
        class Meta:
            model = StudentDetail
            fields = '__all__'