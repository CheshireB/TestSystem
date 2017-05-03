from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from random import sample
from testsystem.models import Subject, tasks, temp_test


@api_view(['GET'])
def subjects(request): #Distinct не работает в SQLlite!!
    data = Subject.objects.all()
    sup = []
    response = []
    for i in data:
        if i.subjecteng not in sup:
            sup.append(i.subjecteng)
            dic = {}
            dic['name'] = i.subject
            dic['nameQuery'] = i.subjecteng
            response.append(dic)
    return  Response(response)


@api_view(['GET'])
def getinfosubject(request):
    subject = request.GET.get('subject')
    dataSub = Subject.objects.filter(subjecteng=subject)
    response = []
    for i in dataSub:
        dic = {}
        dic['id'] = i.typeoftask
        dic['name'] = i.nameoftask
        dic['max_value'] = len(tasks.objects.filter(type_task=i.typeoftask))
        response.append(dic)
    return  Response(response)

@api_view(['GET'])
def getinfostest(request):
    subject = request.GET.get('subject')
    data = tasks.objects.filter(subject_id=subject)
    response = []
    sup = []
    for i in data:
        if i.test_id not in sup:
            sup.append(i.test_id)
            dic = {}
            dic['id'] = str(i.id)
            dic['number'] = str(len(sup))
            response.append(dic)
    return  Response(response)


@api_view(['GET'])
def static(request):
    id = request.GET.get('id')
    subject = request.GET.get('subject')
    data = tasks.objects.filter(subject_id=subject, test_id=int(id)).order_by('type_task')
    order = 1
    response = []
    for i in data:
        dic = {}
        dic['id'] = i.id
        dic['order'] = order
        dic['text'] = i.task
        dic['image'] = "NULL"
        order += 1
        response.append(dic)
    return Response(response)


@api_view(['GET'])
def check(request):
    id = [int(i) for i in request.GET.getlist('id')]
    answer = request.GET.getlist('answer')
    if len(id) != len(answer):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    dicAns, dic = {}, {}
    response = [' ']*len(id)
    k = 0
    data = tasks.objects.filter(id__in=id)
    for i in range(len(id)):
        dicAns[id[i]] = answer[i]
    for i in data:
        dic['id'] = i.id
        dic['answer'] = True if i.answer == dicAns[i.id] else False
        response[k] = dic
    return Response(response)


@api_view(['GET'])
def solve(request):
    id = [int(i) for i in request.GET.getlist('id')]
    response = [' ']*len(id)
    k = 0
    data = tasks.objects.filter(id__in=id)
    for i in data:
        dic = {}
        dic['id'] = i.id
        dic['solve'] = i.solve
        dic['img'] = "NULL"
        response[k] = dic
        k += 1
    return Response(response)


@api_view(['GET'])
def ncustom(request):
    subject = request.GET.get('subject')
    count = [int(i) for i in request.GET.getlist('count')]
    response = []
    order = 0
    for i in range(len(count)):
        data = tasks.objects.filter(type_task=i+1, subject_id=subject)
        print(data)
        try:
            id = sample((0, len(data)-1), count[i])
        except: return Response(status=status.HTTP_400_BAD_REQUEST)
        data = [data[i] for i in id]
        for j in data:
            dic = {}
            dic['id'] = j.id
            dic['order'] = order
            dic['task'] = j.task
            dic['img'] = "NULL"
            order += 1
            response.append(dic)
            print(response)
    p = temp_test(tasks='&'.join([str(i['id']) for i in response]), subject=subject)
    p.save()
    return Response(response)




