from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'contractor',
        'title',
        'supervisor',
        'image',
    )

    ordering = ('-name',)


admin.site.register(User, UserAdmin)
