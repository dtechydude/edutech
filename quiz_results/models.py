from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User
from students.models import StudentDetail

# Create your models here.

class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject =  models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='subject', null=True)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)

    @property
    def exam_score(self):
       return self.score * (60/100)

    @property
    def ca_score(self):
       return self.score * (40/100)



