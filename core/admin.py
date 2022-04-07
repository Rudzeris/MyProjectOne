from django.contrib import admin
import core.models
# Register your models here.
admin.site.register(core.models.Student)
admin.site.register(core.models.Lessons)
admin.site.register(core.models.Exam)