from django.contrib import admin
from .models import Teachers, Student


class StudentInline(admin.TabularInline):
    model = Student

class TeachersAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]
    list_display = ("staff_no", "first_name", "last_name", "levels", "class_held")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_no", "first_name", "last_name", "student_class")

admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Student, StudentAdmin)
