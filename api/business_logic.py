from datetime import timedelta
from django.utils import timezone
from api.services import get_usd_conversion
from .models import Payment
import logging

def get_rejected_payments(user, days):
    return Payment.objects.filter(
        user=user, 
        status=Payment.PaymentStatus.REJECTED,
        date__gte=timezone.now() - timedelta(days=days)
    ).count()

def calculate_total_amount(user, days, service=get_usd_conversion):
    payments = Payment.objects.filter(
        user=user, 
        status=Payment.PaymentStatus.COMPLETED,
        date__gte=timezone.now() - timedelta(days=days)
    )
    total_amount_n_days = 0
    for payment in payments:

        try:
            conversion_amount = service(payment.local_total, payment.local_currency)
        except ValueError as ve:
            raise ValueError(f"Error processing payment {payment.id} with amount {payment.local_total}: {ve}")
        except Exception as e:
            raise Exception(f"Unexpected error processing payment {payment.id}: {e}")

        total_amount_n_days += conversion_amount
    
    return total_amount_n_days
