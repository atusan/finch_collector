from django.contrib import admin
from .models import Art,Feeding,Location

# Register your models here.
admin.site.register(Art)


# register the new Feeding Model 
admin.site.register(Feeding)
admin.site.register(Location)
