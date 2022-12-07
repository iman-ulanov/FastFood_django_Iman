from django.contrib import admin

from .models import *


admin.site.register(Client)
admin.site.register(Worker)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(FoodOrder)

