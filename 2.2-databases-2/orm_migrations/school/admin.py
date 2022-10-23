from django.contrib import admin

from .models import Student, Teacher

class StudentsInline(admin.TabularInline):
    model = Teacher.students.through
    extra = 0

class TeacherInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    list_filter = ['group']
    inline = [TeacherInline, ]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    inlines = [StudentsInline,]
