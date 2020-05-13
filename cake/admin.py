from django.contrib import admin

# Register your models here.
from django.forms import BaseInlineFormSet

from cake.models import Cake, Position


class PositionInlineFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(PositionInlineFormset, self).__init__(*args, **kwargs)
        self.can_delete = False


class PositionInline(admin.TabularInline):
    model = Position
    fields = ('position',)
    readonly_fields = ('position',)
    formset = PositionInlineFormset


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'text')
    list_display = ('id', 'name', 'text')
    inlines = [PositionInline]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    readonly_fields = ('cake',)


