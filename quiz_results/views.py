from django.shortcuts import render
from quiz_results.models import QuizResult
from students.models import StudentDetail
from django.contrib.auth.decorators import login_required
from .filters import QuizResultFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.http import FileResponse
import csv
import os
from django_filters.views import FilterView


# Create your views here.

@login_required
def quizresultlist(request):
    quizresultlist = QuizResult.objects.all()
    quizresult_filter = QuizResultFilter(request.GET, queryset=quizresultlist) 
    quizresultlist = quizresult_filter.qs
    
    # PAGINATOR METHOD
    page = request.GET.get('page', 1)
    paginator = Paginator(quizresultlist, 50)
    try:
        quizresultlist = paginator.page(page)
    except PageNotAnInteger:
        quizresultlist = paginator.page(1)
    except EmptyPage:
       quizresultlist = paginator.page(paginator.num_pages)

    context = {
        'quizresultlist' : QuizResult.objects.all(),
        'quizresult_filter': quizresult_filter,
        'quizresultlist': quizresultlist,

    }
    return render (request, 'quiz_results/quiz_result_list.html', context)


def quizresults_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename=quiz_results.csv'
    
# Create a csv writer
    writer = csv.writer(response)

    quizresults = QuizResult.objects.all()
    
    # Add column headings to the csv files
    writer.writerow(['USERNAME',  'CURRENT CLASS', 'EXAM', 'SESSION', 'TERM', 'SUBJECT', 'SCORE 100%', '60%', '40%', ])


    # Loop thru and output
    for r in quizresults:
        writer.writerow([r.user,  r.user.studentdetail.current_class.name, r.quiz.exam_name, r.quiz.session.name, r.quiz.term,
                        r.quiz.subject_name, r.score, r.exam_score, r.ca_score,])
        
    return response