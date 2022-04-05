import django_filters

import core.models


class StudentFilters(django_filters.FilterSet):
    name = django_filters.Filter(lookup_expr='icontains')
    class Meta:
        model = core.models.Student
        fields = '__all__'