from django.contrib import admin

from .models import Item
from .models import Supplier

class ItemAdmin(admin.ModelAdmin):
	list_display = ['title','amount','availability']
class SupplierAdmin(admin.ModelAdmin):
	list_display = ['name','location','ratings']

admin.site.register(Item, ItemAdmin)
admin.site.register(Supplier, SupplierAdmin)