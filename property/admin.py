from django.contrib import admin

# Register your models here.
from .models import property , catagory , Reserve


admin.site.register(property)
admin.site.register(catagory)
admin.site.register(Reserve)