from nturl2path import url2pathname
from urllib.parse import urlparse
from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('nosotros', views.nosotros, name='nosotros'),

    path('libros', views.libros, name='libros'),

    path('libros/crear', views.crear, name='crear'),

    path('libros/editar', views.editar, name='editar'),

    path('eliminar/<int:id>', views.eliminar, name='eliminar'),

   

] + static(settings.IMAGENES_URL, document_root=settings.IMAGENES_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.IMAGENES_URL, document_root=settings.IMAGENES_ROOT)