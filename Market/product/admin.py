from django.contrib import admin
from .models import product_model

class model_admin(admin.ModelAdmin):
    list_display = ('name','price','stock')

admin.site.register(product_model,model_admin)
