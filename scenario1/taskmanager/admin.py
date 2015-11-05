from django.contrib import admin

from .models import Todolist, Task

# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task
    extra = 3

class TodolistAdmin(admin.ModelAdmin):
#    fieldsets = [
#                 (None,               {'fields': ['question_text']}),
#                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#                 ]
    inlines = [TaskInline]
    list_display = ('Title', 'pub_date')

admin.site.register(Todolist, TodolistAdmin)
admin.site.register(Task)