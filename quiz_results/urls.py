from django.urls import path
from django.conf.urls.static import static
from quiz_results import views as quizresult_views 
from django.contrib.auth import views as auth_views
# from .views import QuizResultListView


app_name = 'quiz_results'

urlpatterns = [
    path('quiz-result/', quizresult_views.quizresultlist, name="quiz-result-list"),
    path('quiz-result-csv', quizresult_views.quizresults_csv, name="quiz-result-csv"),
 
    # path('quiz-result/', QuizResultListView.as_view(), name="quiz-result"),


]