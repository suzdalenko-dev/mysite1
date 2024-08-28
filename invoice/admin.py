from django.contrib import admin
from .models.company import Company
from .models.country import Country
from .models.factura import Factura
from .models.article import Article
from .models.customer import Customer
from .models.vehicledata import Vehicledata

# Register your models here.

admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Factura)
admin.site.register(Article)
admin.site.register(Customer)
admin.site.register(Vehicledata)