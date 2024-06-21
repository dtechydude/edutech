from django.urls import path
#from wkhtmltopdf.views import PDFTemplateView
#from wkhtmltopdf import PDFTemplateView
from wkhtmltopdf import WKHtmlToPdf
from django.conf.urls.static import static
from results import views as result_views 
from django.contrib.auth import views as auth_views
from . import views
from .views import ResultListView, ResultDetailView, ResultUpdateView
# from . import views

app_name = 'results'

urlpatterns = [
    path('print-result/', result_views.printresult, name="print-result"),
    path('result-sheet/', result_views.resultsheet, name="result-sheet"),
    path('result-create/', result_views.result_create_form, name="result-create"),
    path('my-result/', result_views.view_self_result, name="my-result"),

    path('print-resultform/', result_views.printresultform, name="print-resultform"),
    path('upload-result/', result_views.uploadresult, name="upload-result"),
   
    path('my-reportsheet/', result_views.view_self_reportsheet, name="my-reportsheet"),

    # path('<int:pk>/', ResultDetailView.as_view(), name='result_detail'),
    path('<int:id>/result-update/', ResultUpdateView.as_view(), name="result-update"),

    path('result-list/', ResultListView.as_view(), name='result-list'),
    path('<int:pk>/', ResultDetailView.as_view(), name='result-detail'), 
    path('result-csv', result_views.results_csv, name="result-csv"),
 
    # render resultsheet as pdf
    path('pdf/<pk>/', result_views.result_render_pdf_view, name="result-pdf-view"),
    #path('results/', PDFTemplateView.as_view(template_name='results/result_sheet.html',
    #                                       filename='my_result.pdf'), name='result-pdf'),

    
]
    # path('self-result/', views.SelfResultListView.as_view(), name='self-result'),
    