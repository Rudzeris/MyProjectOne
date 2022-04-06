from django.urls import path
import core.views
from django.contrib import admin

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('admin/', core.views.IndexView.as_view(), name='admin'),
    path('list/', core.views.Student_list.as_view(), name='Student_list'),
    path('list/<int:pk>/', core.views.Exam_list.as_view(), name='Exam_list'),
    path('list/create/', core.views.StudentCreate.as_view(), name='Student_create'),
    path('list/<int:pk>/update/', core.views.StudentUpdate.as_view(), name='Student_update'),
    path('list/<int:pk>/delete/', core.views.StudentDelete.as_view(), name='Student_delete'),
]