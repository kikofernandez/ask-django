from django.contrib import admin

# Register your models here.
from .models import Service, Skill, Rating

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['user_request', 'state', 'priority', 'no_people', 'cancellable', 'short_description']

    def short_description(self, obj):
        return obj.request[:100]+"..."

class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating', 'service', 'requester', 'performer']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill)
admin.site.register(Rating, RatingAdmin)