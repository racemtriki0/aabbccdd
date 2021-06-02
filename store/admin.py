from django.contrib import admin
from . models import  Fournisseurr, Product, Size, OtherImages

# Register your models here.
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(OtherImages)
admin.site.register(Fournisseurr)