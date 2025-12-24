from django.contrib import admin
from .models import Menu, Category, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'price', 'rating', 'category')

admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
