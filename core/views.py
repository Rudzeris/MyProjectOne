from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
import core.models

class IndexView(TemplateView):
    template_name = 'core/index.html'


def Student_list(request):
    name = request.GET.get('name')
    students = core.models.Student.objects.all()

    if name:
       students = students.filter(name__icontains=name)

    return render(request, 'core/student_list.html', {'object': students})



def Exam_list(request, pk):
    exam=core.models.Exam.objects.all().filter(student_id=pk)
    return render(request, 'core/exam_list.html', {'exam': exam})

