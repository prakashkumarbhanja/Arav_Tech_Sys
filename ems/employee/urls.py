from django.urls import path

from employee import views

urlpatterns = [
    path('', views.test, name='test'),
    path('add/', views.employe_add, name='employe_add'),
]