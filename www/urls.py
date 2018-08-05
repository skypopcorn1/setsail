from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name="home"),
	# path(r'create/$', views.create_races),
	# path(r'read/$', views.read_races, name="read"),
    # path(r'delete/', views.delete_races),
    # path(r'(?P<slug>[-_\w]+)/$', views.posts_detail, name='detail'),
    # path(r'(?P<slug>[-_\w]+)/update/$', views.posts_update, name='update'),

    ]
