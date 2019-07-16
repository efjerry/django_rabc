from django.contrib import admin
from rbac import models


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'url','name']  # 写入要展示的字段
    list_editable = ['url','name']  # 写入要编辑的字段


admin.site.register(models.Role)
admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.User)
admin.site.register(models.Menu)