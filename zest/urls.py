from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name='home' ),
    path('generate_pid/', views.generate_pid, name='generate_pid' ),
    path('search_pid/<int:roll_no>/', views.search_pid_by_roll, name='search_pid_by_roll'),
    path('search_pid/', views.search_pid, name='search_pid' ),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
]
