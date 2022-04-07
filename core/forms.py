from django import forms

import core.models


class StudentSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)


class StudentEdit(forms.ModelForm):
    class Meta:
        model = core.models.Student
        fields = '__all__'

class LessonEdit(forms.ModelForm):
    class Meta:
        model = core.models.Lessons
        fields = '__all__'