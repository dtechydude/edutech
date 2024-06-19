from django.contrib import admin
from users.models import Profile


class UserProfileAdmin(admin.ModelAdmin):
       
    list_display=('user', 'code', 'user_type')
    list_filter  = ['user_type',]
    search_fields = ('user__username', 'code', 'user_type')


# Register your models here.
admin.site.register(Profile, UserProfileAdmin)
