from django.contrib import admin
from.models import Items,Category,Subcategory,slider,ad,Contact
# Register your models here.

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Items)
admin.site.register(slider)
admin.site.register(Contact)
admin.site.register(ad)