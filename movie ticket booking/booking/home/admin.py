from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MovieCategory)
admin.site.register(Movie)
admin.site.register(Cart)
admin.site.register(CartItems)

