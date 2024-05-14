from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<str:pk>/', views.news, name='news'),
    path('', views.times1, name='times1'),
    path('', views.times2, name='times2'),
    path('', views.times3, name='times3'),
    path('', views.times4, name='times4'),
]