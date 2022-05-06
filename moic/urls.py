from django.urls import path
from . import views

app_name = 'moic'
urlpatterns = [
path('', views.index, name='index'),
path('home', views.home, name='home'),
path('mission', views.mission, name='mission'),
path('dirigeants', views.dirigeants, name='dirigeants'),
path('conference', views.conference, name='conference'),
path('peace', views.peace, name='peace'),
path('simulation', views.simulation, name='simulation'),
path('sustainable', views.sustainable, name='sustainable'),
path('involved', views.involved, name='involved'),
path('corona', views.corona, name='corona'),
path('humanity', views.humanity, name='humanity'),
]