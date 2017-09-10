from django.contrib import admin

from .models import DetalleVenta, Venta


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta


class VentaAdmin(admin.ModelAdmin):

    raw_id_fields = ('cliente',)
    inlines = (DetalleVentaInline,)
    exclude = ['vendedor', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.vendedor = request.user
        obj.save()
admin.site.register(Venta, VentaAdmin)