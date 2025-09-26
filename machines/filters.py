import django_filters
from .models import Machine

class MachineFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(method='filter_by_tags')

    class Meta:
        model = Machine
        fields = ['difficulty', 'tags']

    def filter_by_tags(self, queryset, name, value):
        # Filtra por nombre de tag exacto
        return queryset.filter(tags__name__iexact=value)
