from django.contrib import admin

from .models import Orders
from .models import Orders_Item

# Register your models here.
admin.site.register(Orders)
admin.site.register(Orders_Item)