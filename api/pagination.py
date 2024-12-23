from rest_framework.pagination import LimitOffsetPagination

class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100


from rest_framework.pagination import PageNumberPagination

class CategoryPageNumberPagination(PageNumberPagination):
    page_size = 10
