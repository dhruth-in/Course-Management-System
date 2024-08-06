from django.contrib import admin 
from django.urls import path 
from course_app.views import StudentDetailView, StudentListView, add_project, course_search, course_search_ajax, home, reg, regaj
from course_management import settings 
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="Admin Login"  
admin.site.site_title="Course Management"  
admin.site.index_title="Course Management" 

urlpatterns = [
    path('', home, name='home'),  # Homepage URL
    path('admin/', admin.site.urls),
    path('reg/', reg, name='reg'),
    path('course_search/', course_search, name='course_search'),
    path('add_project/', add_project, name='add_project'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('regaj/', regaj, name='regaj'),
    path('course_search_ajax/', course_search_ajax, name='course_search_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)