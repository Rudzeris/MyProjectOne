from django.urls import path
import core.views
from django.contrib import admin

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('admin/', core.views.IndexView.as_view(), name='admin'),
    path('list/student/', core.views.Student_list.as_view(), name='Student_list'),
    path('list/lesson/', core.views.Lesson_list.as_view(), name='Lesson_list'),
    path('list/student/<int:pk>/', core.views.Exam_list.as_view(), name='Exam_list'),
    path('list/student/create/', core.views.StudentCreate.as_view(), name='Student_create'),
    path('accounts/login/', core.views.LoginView.as_view(), name="login"),
    path('accounts/profile/', core.views.ProfilePage.as_view(), name="profile"),
    path(r'^accounts/register/$', core.views.RegisterView.as_view(), name="register"),
]