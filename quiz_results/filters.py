import django_filters
from .models import QuizResult
from django.contrib.auth.models import User

class QuizResultFilter(django_filters.FilterSet):

    class Meta:
        model = QuizResult
        # # fields = '__all__'
        # fields = {'current_class': ['exact']}
        fields = {'quiz', 'subject',}
        

