
from django.shortcuts import render_to_response, HttpResponse


from .models import tasks, Subject


def index(request):
    return render_to_response('testsystem/index.html')


def info_subject(request, subject_t):
    args = {}
    args['nameoftasks'] = Subject.objects.filter(subjecteng=subject_t).order_by('typeoftask')
    args['subjecteng'] = subject_t;
    args['xrange'] = ['1','2','3','4','5','6']
    args['urlcss'] = 'testsystem/css/'+subject_t+".css"
    return render_to_response('testsystem/subject.html', args)

def static_test(request, subject_t, id):
    args = {}
    args['queryset'] = tasks.objects.filter(test_id=id, subject_id=subject_t)
    try:
        args['queryset'][len(Subject.objects.filter(subjecteng=subject_t))-1].id
    except:
        return HttpResponse("Bad request")
    args['subject'] = Subject.objects.filter(subjecteng=subject_t)[0].subject
    args['testid'] = id
    return render_to_response('testsystem/test.html', args)

def get_new_temp_test(request):
    return HttpResponse("LOOOOOOOOL")






