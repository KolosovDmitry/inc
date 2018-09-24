from django.shortcuts import render, redirect

# Create your views here.


def home(request):
	if request.user.is_active:
		return render(request, 'home.html',)
	else:
		return redirect('api.auth_reg:login')