from django.urls import path
import core.views
from django.contrib import admin

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', core.views.Hi, name='index'),
    # path('', core.views.IndexView.as_view(), name='index'),
]