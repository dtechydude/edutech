from django.db import models
import random
from curriculum.models import Standard, Session

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    exam_name = models.CharField(max_length=120)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='session_quiz', null=True)
    first_term = 'First Term'
    second_term = 'Second Term'
    third_term = 'Third Term'
    others = 'Others'

    term_status = [
        (first_term, 'First Term'),
        (second_term, 'Second Term'),
        (third_term, 'Third Term'),
        (others, 'Others'),

    ]

    term = models.CharField(max_length=15, choices=term_status, default='First Term')
    subject_name = models.CharField(max_length=120)
    standard =  models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='standard', null=True)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.exam_name}-{self.subject_name} - {self.standard}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'