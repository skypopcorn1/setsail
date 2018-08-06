from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name="home"),
    path(r'club/registration/', views.clubRegistration, name="club_registration"),
	# path(r'create/$', views.create_races),
	# path(r'read/$', views.read_races, name="read"),
    # path(r'delete/', views.delete_races),
    ]
