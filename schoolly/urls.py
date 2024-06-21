from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url
from django.views.static import serve

# from attendance.views import AttendanceAutocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curriculum/', include('curriculum.urls', namespace='curriculum')),
    path('', include('pages.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('users/', include('users.urls')),
   
    path('results/', include('results.urls', namespace='results')),
    path('students/', include('students.urls', namespace='students')),
    path('staff/', include('staff.urls', namespace='staff')),

    path('attendance/', include('attendance.urls', namespace='attendance')),
    # path('demoschool/', include('demoschool.urls', namespace='demoschool')),
    path('portal/', include('portal.urls', namespace='portal')),
    path('quizes/', include('quizes.urls', namespace = 'quizes')),
    path('blog/', include('blog.urls', namespace = 'blog')),
    path('notification/', include('notification.urls', namespace = 'notification')),
    path('inventory/', include('inventory.urls', namespace = 'inventory')),
    path('quiz_results/', include('quiz_results.urls', namespace = 'quiz_results')),
    # path('demoschool/', include('demoschool.urls')),
   

    # path('ckeditor', include('ckeditor_uploader.urls')),    #for ckeditor image upload
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    


    

#PATH FOR DOWNLOAD URL
   #url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
   #path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),


#    url( r'^attendance-autocomplete/$', AttendanceAutocomplete.as_view(), name='attendance-autocomplete',
#     ),

  path('djrichtextfield/', include('djrichtextfield.urls')),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)