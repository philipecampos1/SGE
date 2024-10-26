from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/list/', views.SuppliersListView.as_view(), name='supplier_list'),
    path('suppliers/create/', views.SuppliersCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/detail/', views.SuppliersDetailView.as_view(), name='supplier_detail'),
    path('suppliers/<int:pk>/update/', views.SuppliersUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.SuppliersDeleteView.as_view(), name='supplier_delete'),

    path('api/v1/suppliers/', views.SupplierCreateListAPIView.as_view(), name='supplier-create-list-api-view'),
    path('api/v1/suppliers/<int:pk>/', views.SupplierRetriveUpdateDestroyAPIView.as_view(), name='supplier-detail-api-view')

]
