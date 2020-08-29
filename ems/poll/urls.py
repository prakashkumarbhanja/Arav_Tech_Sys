from django.urls import path

from poll import views
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    path('<int:id>', views.poll, name='single_poll'),
]