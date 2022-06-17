
from django.contrib import admin
from django.urls import path
from product.views import x

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',x)
]
