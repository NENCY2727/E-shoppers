from django.contrib import admin # type: ignore
from .models import*

# Register your models here.
admin.site.register(Employee)
admin.site.register(registeruser)
admin.site.register(category)
admin.site.register(subcategory)
admin.site.register(colorfilter)
