from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
import core.models
import core.filters


class IndexView(TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Главная страница'


class Student_list(ListView):
    queryset = core.models.Student.objects.all()

    def get_filters(self):
        return core.filters.StudentFilters(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        context['filters'] = self.get_filters()
        return context


class Exam_list(ListView):
    queryset=core.models.Exam.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        s=1
        queryset = core.models.Exam.objects.all()
        if pk:
            queryset = queryset.filter(student_id=pk)
        return queryset

