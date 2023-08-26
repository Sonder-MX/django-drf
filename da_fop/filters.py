from django_filters import rest_framework as filters

from .models import Person


class PersonFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")  # 模糊查询
    gender = filters.CharFilter(field_name="gender", lookup_expr="exact")  # 精确查询
    start_birthday = filters.DateFilter(field_name="birthday", lookup_expr="gte")  # 大于等于
    end_birthday = filters.DateFilter(field_name="birthday", lookup_expr="lte")  # 小于等于
    ages = filters.BaseInFilter(field_name="age", lookup_expr="in")  # in查询
    sort = filters.OrderingFilter(fields=("age", "created", "birthday"))  # 排序

    # 自定义方法查询 eg:
    # name = filters.CharFilter(field_name="name", method="filter_name")  # 自定义查询方法

    # def filter_name(self, queryset, name, value):
    #     """
    #     @params queryset: Person.objects.all()
    #     @params name: 参数名称，即field_name
    #     @params value: 前端传过来的值
    #     """
    #     return queryset.filter(name__icontains=value)

    class Meta:
        model = Person
        fields = ["name", "gender", "start_birthday", "end_birthday", "ages", "sort"]
