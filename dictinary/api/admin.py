from django.contrib import admin
from .models import Worlds
# Register your models here.

@admin.register(Worlds)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = [
       'world',

    ]
    search_fields = [
        "name", 
     
    ]