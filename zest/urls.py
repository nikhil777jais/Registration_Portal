from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('generate_pid/', views.generate_pid, name='generate_pid' ),
    path('search_pid/<int:roll_no>/', views.search_pid_by_roll, name='search_pid_by_roll' ),
    path('search_pid/', views.search_pid, name='search_pid' ),
]
