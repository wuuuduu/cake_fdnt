from django.contrib import admin

# Register your models here.
from cake.models import Cake, Position

admin.site.register(Cake)
admin.site.register(Position)