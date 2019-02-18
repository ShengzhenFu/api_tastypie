from django.contrib import admin
from services.models import Product, Order, Team, TechnicalService, Server

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Team)
admin.site.register(TechnicalService)
admin.site.register(Server)
