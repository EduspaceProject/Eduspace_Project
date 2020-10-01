from django.contrib import admin
from .models.user import user_login,user,education_detail,graduation

admin.site.register(user_login)
admin.site.register(user)
admin.site.register(education_detail)
admin.site.register(graduation)
# Register your models here.
