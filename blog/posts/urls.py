from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<slug:slug>/', views.post, name='post'),
]
