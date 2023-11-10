from django.contrib import admin
from userauths.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','payment_status','address']

admin.site.register(User, UserAdmin)


