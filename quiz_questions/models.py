from django.db import models
from quizes.models import Quiz
#from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Question(models.Model):
    # text = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.text}"

    def get_answers(self):
        return self.answer_set.all()


    @property
    def html_stripped(self):
        return strip_tags(self.text)



class Answer(models.Model):
    text = models.CharField(max_length=200)
    text_2 = CKEditor5Field('Text', config_name='extends')
    # text = RichTextField(blank=True, null=True)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"




