from django.contrib import admin

# Register your models here.
from .models import User, Application, Status

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'telephone']
    list_display_links = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'telephone']
    list_filter = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'telephone']
    search_fields = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'telephone']

admin.site.register(User,UserAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'car_number', 'description', 'status', 'date_of_submission', 'image']
    list_display_links = ['user', 'car_number', 'description', 'status', 'date_of_submission', 'image']
    list_filter = ['status', 'date_of_submission']
    search_fields = ['user', 'car_number', 'description', 'status', 'date_of_submission']
    readonly_fields = ['image']

admin.site.register(Application, ApplicationAdmin)


admin.site.register(Status)
