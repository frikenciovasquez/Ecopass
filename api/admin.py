from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin

from .models import Blog,Destiny,Rental,Rute,Service,Travel,User
# Register your models here.

admin.site.register(Blog)
admin.site.register(Destiny)
admin.site.register(Rental)
admin.site.register(Rute)
admin.site.register(Service)
admin.site.register(Travel)
admin.site.register(User)

'''
USER = get_user_model()


@admin.register(USER)
class UserAdmin(auth_admin.UserAdmin):
    """ Register User model within django admin panel. """

    model = USER
    fieldsets = (
        ('Datos personales', {
            'fields': (
                'username', 'email', 'password'
             ),
        }),
    )

'''
