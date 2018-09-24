from django.contrib import admin
from import_export import resources
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(Profile, ProfileAdmin)