from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
import core.models
import core.filters
import core.forms

class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context

class IndexView(TitleMixin,TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Главная страница'


class Student_list(TitleMixin,ListView):
    queryset = core.models.Student.objects.all()
    title = 'Студенты'
    def get_filters(self):
        return core.filters.StudentFilters(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        # context['filters'] = self.get_filters()
        context['form'] = core.forms.StudentSearch(self.request.GET or None)
        return context


class Exam_list(TitleMixin,ListView):
    queryset=core.models.Exam.objects.all()
    title='Информация'
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        s=1
        queryset = core.models.Exam.objects.all()
        if pk:
            queryset = queryset.filter(student_id=pk)
        return queryset


class StudentUpdate(TitleMixin, UpdateView):
    model = core.models.Student
    form_class = core.forms.StudentEdit

    def get_title(self):
        return f'Изменение данных студента "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('Student_list')


class StudentCreate(TitleMixin, CreateView):
    model = core.models.Student
    form_class = core.forms.StudentEdit
    title = 'Добавление Студента'

    def get_success_url(self):
        return reverse('core:Student_list')


class StudentDelete(TitleMixin, DeleteView):
    model = core.models.Student

    def get_title(self):
        return f'Отчисление студента {str(self.get_object())}'

    def get_success_url(self):
        return reverse('core:Student_list')