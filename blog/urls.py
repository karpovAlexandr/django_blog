from django.urls import path

from .views import Home, PostsByCategory, GetPost, PostsByTag, Search

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # чтоб все работало, нужен метод get_absolute_url у класса в models
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
]
