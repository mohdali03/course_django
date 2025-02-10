from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display= ('username','email','user_type')
# Register your models here.

admin.site.register(CustomUser, UserAdmin )
