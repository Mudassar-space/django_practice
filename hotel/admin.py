from django.contrib import admin
from .models import HotelModel
# Register your models here.
@admin.register(HotelModel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'branch_no']