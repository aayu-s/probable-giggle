from typing import List
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from todo.models import List, Status, Item

class ItemInLine(admin.TabularInline):
    model = Item
    readonly_fields = ('created_at', 'updated_at')


@admin.register(List)
class ListAdmin(ModelAdmin):
    list_display = ('name', 'owner')
    inlines = [
        ItemInLine,
    ]
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name','owner__username')
    list_filter = ('owner',)

@admin.register(Status)
class StatusAdmin(ModelAdmin):
    list_display = ('name', 'is_endstatus')
    list_filter = ('is_endstatus',)

