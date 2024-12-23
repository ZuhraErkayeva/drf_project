from django.urls import path
from .views import PostCreateAPIView,CategoryCreateAPIView


urlpatterns = [
    path('posts/',PostCreateAPIView.as_view()),
    path('categories/', CategoryCreateAPIView.as_view()),
]