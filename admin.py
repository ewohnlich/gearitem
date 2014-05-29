from django.contrib import admin

# Register your models here.
from gearitem.models import GearItem,Comment

admin.site.register(GearItem)
admin.site.register(Comment)