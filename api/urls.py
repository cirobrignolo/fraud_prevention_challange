from django.urls import path
from .views import fraud_check

urlpatterns = [
    path('fraud-check/<uuid:user_id>/', fraud_check, name='fraud-check'),
]