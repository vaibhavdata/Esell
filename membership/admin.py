from django.contrib import admin
from .models import *
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('id', 'username', 'email')
    
    list_display = ('username', 'id', 'email','phone_number','date_joined')
    