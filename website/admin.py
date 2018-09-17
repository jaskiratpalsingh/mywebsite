from django.contrib import admin
from .models import Customer,Product,SoldProduct,OrderedProduct

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(SoldProduct)
admin.site.register(OrderedProduct)

