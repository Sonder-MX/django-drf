from rest_framework.pagination import PageNumberPagination


class PersonPagination(PageNumberPagination):
    page_size = 10  # 每页显示10条
    max_page_size = 20  # 每页最多显示20条
    page_size_query_param = "size"  # 每页显示条数的参数名
    page_size_query_description = "每页显示条数，最多显示20条"  # 每页显示条数的描述信息
