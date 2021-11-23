from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name='home' ),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('generate_pid/', views.generate_pid, name='generate_pid' ),
    path('search_pid/', views.search_pid, name='search_pid' ),
    path('search_pid/<int:roll_no>/', views.search_pid_by_roll, name='search_pid_by_roll'),
    path('generate_tid/', views.generate_tid, name='generate_tid' ),
    path('add_pid_in_tid/<int:tid>/', views.add_pid_in_tid, name='add_pid_in_tid' ),
    path('search_tid/', views.search_tid, name='search_tid' ),
    path('register_event/', views.register_event, name='register_event' ),
    path('add_event_in_pid/', views.add_event_in_pid, name='add_event_in_pid'),
    path('add_event_in_tid/', views.add_event_in_tid, name='add_event_in_tid'),
    path('event_summary/', views.event_summary, name='event_summary'),
    path('event_details/<int:id>/', views.event_details, name='event_details'),
    path('t_event_details/<int:id>/', views.t_event_details, name='t_event_details'),
]
