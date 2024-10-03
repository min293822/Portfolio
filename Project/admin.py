from django.contrib import admin
from .models import UserDetails

class UserDatailView(admin.ModelAdmin):
  list_display = ('user', 'sex', 'email')

admin.site.register(UserDetails, UserDatailView)

# Register your models here.
