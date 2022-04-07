from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render, redirect
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


class StudentCreate(TitleMixin, CreateView):
    model = core.models.Student
    form_class = core.forms.StudentEdit
    title = 'Добавление Студента'

    def get_success_url(self):
        return reverse('core:Student_list')


class Lesson_list(TitleMixin,ListView):
    queryset = core.models.Lessons.objects.all()
    title = 'Предметы'

class LoginView(TemplateView):
    template_name = "core/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:profile")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class ProfilePage(TemplateView):
    template_name = "core/profile.html"


class RegisterView(TemplateView):
    template_name = "core/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)