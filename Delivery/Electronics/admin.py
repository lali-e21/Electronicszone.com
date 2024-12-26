from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib import admin
from .models import Laptop, Mobile,Earphone,Charger

@admin.register(Laptop)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('Number','Name', 'Price', 'Brand', 'Screen_Size')
    search_fields = ('Name', 'Brand')


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('Number','Mobile_Name', 'Price', 'Brand', 'Android', 'Battery')
    search_fields = ('Mobile_Name', 'Brand')

@admin.register(Earphone)
class EarphoneAdmin(admin.ModelAdmin):
    list_display = ('Number','Earphone_Name', 'Price', 'Brand', 'Waranty')
    search_fields = ('Earphone_Name', 'Brand')

@admin.register(Charger)
class EarphoneAdmin(admin.ModelAdmin):
    list_display = ('Number','Charger_Name', 'Price', 'Brand', 'Waranty')
    search_fields = ('Charger_Name', 'Brand')
    
