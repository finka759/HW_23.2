from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', products, name='index'),
    path('index', products, name='index'),
    path('products', products, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product, name='product'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
