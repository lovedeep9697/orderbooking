from django.contrib import admin
import orderbook.models as models

# Register your models here.
admin.site.register(models.Token)
admin.site.register(models.Order)
admin.site.register(models.Trade)
