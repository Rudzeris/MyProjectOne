from django.http import HttpResponse
from django.shortcuts import render
import core.models


def index(request):
    return render(request, 'core/index.html')


def Student_list(request):
    students=core.models.Student.objects.all()
    return render(request, 'core/student_list.html', {'object': students})


def Student_detail(request,pk):
    exam=core.models.Exam.objects.get(pk=pk)
    return render(request, 'core/student_list.html', {'exam': exam})

