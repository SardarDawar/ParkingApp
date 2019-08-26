from django.contrib import admin
from .models import parking_slot,parking_daily_history
# Register your models here.


admin.site.register(parking_slot)
admin.site.register(parking_daily_history)
