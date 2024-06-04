from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
                  path('', ProductListView.as_view(), name='index'),
                  path('index/', ProductListView.as_view(), name='index'),
                  path('products/', ProductListView.as_view(), name='index'),
                  path('create/', ProductCreateView.as_view(), name='create'),
                  path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
                  path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
                  path('contacts/', ContactsView.as_view(), name='contacts'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
