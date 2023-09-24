from django.contrib import admin
from.models import *

"""class categoryadmin(admin.ModelAdmin):
    list_display=('name','image','discription')
    admin.site.register(category,categoryadmin)
"""
admin.site.register(category)
admin.site.register(product)
admin.site.register(Favourite)
admin.site.register(Cart)
