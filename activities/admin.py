from django.contrib import admin
from .models import BenchmarkingEntry, MediaMention, Event


@admin.register(BenchmarkingEntry)
class BenchmarkingEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    ordering = ('-date',)
    search_fields = ('title',)


@admin.register(MediaMention)
class MediaMentionAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'date')
    ordering = ('-date',)
    search_fields = ('title', 'source')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    ordering = ('date',)
    search_fields = ('title', 'location')