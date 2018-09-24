from django.urls import path, re_path
from . import views
app_name = 'api.home'
urlpatterns = [
	path('', views.home, name='home'),
	#re_path(r'^$', views.home, name='home')
	
	
]