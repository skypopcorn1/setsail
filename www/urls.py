from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'home/', views.home, name="home"),
    path(r'club/home/', views.club, name="club_home"),
    path(r'club/home/racemanagement/', views.RaceManagement, name="race_management"),
    path(r'club/home/racemanagement/addrace/', views.RaceManagementAdd, name="add_race"),
    path(r'user/login/', views.LoginView, name="user_login"),
    path(r'user/registration/', views.registration, name="club_registration"),
	# path(r'create/$', views.create_races),
	# path(r'read/$', views.read_races, name="read"),
    # path(r'delete/', views.delete_races),
    ]
