from django.urls import path
import core.views
from django.contrib import admin

app_name = 'core'

urlpatterns = [
    path('', core.views.index, name='index'),
    path('list/', core.views.Student_list, name='Student_list'),
    # path('', core.views.IndexView.as_view(), name='index'),
]