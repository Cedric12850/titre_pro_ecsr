from django.contrib import admin
from .models import MindMap

@admin.register(MindMap)
class MindMapAdmin(admin.ModelAdmin):
    list_display = ('title', 'data', 'created_at', 'updated_at')