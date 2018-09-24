from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import forms
from .forms import UserForm
from .forms import ProfileForm
from .models import Profile
from api.job.models import Job
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('api.auth_reg:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    
    
def profile(request):
	if request.user.is_active:
		job_created = Job.objects.filter(created_user = request.user).count()
		job_responsible = Job.objects.filter(responsible = request.user).count()
		content = {"job_created":job_created, 'job_responsible':job_responsible}
		return render(request, 'registration/profile.html', content)
	else:
		return redirect('api.auth_reg:login')
	
	