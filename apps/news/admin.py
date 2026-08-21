from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Newness, Category, Contact


@admin.register(Newness)
class NewnessAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "created_at",
    )
    list_filter = ("status",)
    search_fields = ("title", "content")
    exclude = ("slug",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title",)
    exclude = ("slug",)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'message')