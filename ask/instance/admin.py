from django.contrib import admin

# Register your models here.
from .models import Service, Skill

admin.site.register(Service)
admin.site.register(Skill)
