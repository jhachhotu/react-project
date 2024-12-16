from django.contrib import admin
from .models import PlayerProfile, Event
# Register your models here.

@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'team', 'position')
    search_fields = ('user__username', 'team', 'position')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location')
    search_fields = ('name', 'location')
