from django.contrib import admin
from . import models

admin.site.register(models.Location)
admin.site.register(models.Choice)

admin.site.register(models.PlayerStatus)
admin.site.register(models.Item)