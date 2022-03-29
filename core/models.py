from django.db import models


class Student(models.Model):
    name = models.CharField('ФИО', max_length=128)

    class Meta:
        verbose_name = 'ФИО'
        verbose_name_plural = 'ФИО'


class Lesson(models.Model):
    name = models.CharField('Предмет', max_length=32)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Exam(models.Model):
    student = models.ForeignKey('core.Student', on_delete=models.CASCADE, null=False, blank=True)
    lesson = models.ForeignKey('core.Lesson', on_delete=models.SET_NULL, null=True, blank=True)
    grade = models.IntegerField('Оценка', blank=True, null=True)

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

