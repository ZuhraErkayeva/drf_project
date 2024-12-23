from .serializers import CategorySerializer,PostSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Post,Category
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import PostLimitOffsetPagination,CategoryPageNumberPagination


class PostCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['author']
    search_fields = [ '^title']
    ordering_fields = ['created_at']
    ordering = ['created_at']
    pagination_class = PostLimitOffsetPagination



class CategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^category']
    ordering_fields = ['created_at']
    ordering = ['created_at']
    pagination_class = CategoryPageNumberPagination




