from django.contrib import admin

from .models import Newness, Category

@admin.register(Newness)
class NewnessAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("title", "content")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)