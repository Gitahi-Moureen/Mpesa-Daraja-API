from django.urls import path
from .views import process_payment, mpesa_callback, check_payment_status_view

urlpatterns = [
    path('api/payments/', process_payment, name='process_payment'),
    path('api/payments/callback/', mpesa_callback, name='mpesa_callback'),
    path('api/payments/status/', check_payment_status_view, name='check_payment_status'),
]
