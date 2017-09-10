from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings


# from apps.home.views import (
#     LandingView, HomeView,
#     ContactView, HelpView
#     )

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('apps.inicio.urls',namespace='inicio')),
    
    url(r'^integrations/', include('apps.messenger.urls', namespace="integrations")),
    url(r'', include('apps.proveedor.urls',namespace='proveedor')),
    url(r'', include('apps.cliente.urls',namespace='clientes_app')),
    url(r'', include('apps.producto.urls',namespace='productos')),
    url(r'', include('apps.empleado.urls',namespace='empleados')),
    url(r'', include('apps.venta.urls',namespace='ventas')),
    url(r'', include('apps.repuesto.urls',namespace='repuestos')),
    url(r'', include('apps.propaganda.urls',namespace='propagandas')),


    # URL APPS PROJECT 

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),

]	