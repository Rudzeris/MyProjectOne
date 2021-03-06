from django.db import models


class Student(models.Model):
    name = models.CharField('ФИО', max_length=128)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name


class Lessons(models.Model):
    name = models.CharField('Предмет', max_length=128)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class Exam(models.Model):
    student = models.ForeignKey('core.Student', on_delete=models.CASCADE, null=False, blank=True)
    lesson = models.ForeignKey('core.Lessons', on_delete=models.CASCADE, null=False, blank=True)
    grade = models.IntegerField('Оценка', blank=True, null=True)

    class Meta:
        ordering=['grade']
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

    def __str__(self):
        return self.grade
