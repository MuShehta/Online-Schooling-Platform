from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.Course)
admin.site.register(models.Matrial)
admin.site.register(models.Quiz)
admin.site.register(models.Result)