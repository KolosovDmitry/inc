from django.urls import path, include
from . import views
from django.contrib.auth.views import login as original_login
from django.contrib.auth.views import logout
app_name = 'api.auth_reg'
urlpatterns = [
	path('account/', include('django.contrib.auth.urls')),
	#path('account/login/', views.LoginView, name="account_login"),
	#path('account/signup/', views.SignupView.as_view(), name="account_signup"),
#	path('account/profile/', views.profile, name='profile'),
	path('account/edit_profile/', views.update_profile, name='update_profile'),
	#path('accounts/logout/', views.login, name='logout'),
	
]

