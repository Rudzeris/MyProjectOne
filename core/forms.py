from django import forms

import core.models


class StudentSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)


class StudentEdit(forms.ModelForm):
    class Meta:
        model = core.models.Student
        fields = '__all__'