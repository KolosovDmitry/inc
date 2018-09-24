from django.shortcuts import render, redirect


def index(request):
    if request.user.is_active:
		return render(request, 'home.html',)
	else:
		return redirect('api.auth_reg:login')