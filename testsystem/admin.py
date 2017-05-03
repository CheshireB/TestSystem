from django.contrib import admin
from .models import tasks, Subject


class TasksAdmin(admin.ModelAdmin):

    list_display_links = (
        'id',        'subject_id',
        'type_task', 'task',
        'answer',    'image',
        'solve',     'solve_image',
        'test_id',   'date_pub',
        'flag',)

    list_display = (
        'id',        'subject_id',
        'type_task', 'task',
        'answer',    'image',
        'solve',     'solve_image',
        'test_id',   'date_pub',
        'flag',)


    list_filter = ('subject_id',)

class SubjectAdmin (admin.ModelAdmin):

    list_display_links = ('id',)

    list_display =  (
        'id',
        'typeoftask',
        'nameoftask',
        'subject',
        'subjecteng'
    )


admin.site.register( tasks, TasksAdmin)
admin.site.register( Subject, SubjectAdmin)