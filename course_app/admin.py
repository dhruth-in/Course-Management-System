from django.contrib import admin

from course_app.models import Student, Course

# Register your models here.

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_usn', 'student_sem')
    ordering = ('student_name',)
    search_fields = ('student_name',)

admin.site.register(Course)

