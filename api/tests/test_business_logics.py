from decimal import Decimal
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from api.business_logic import calculate_total_amount, get_rejected_payments
from api.models import Payment, User

class MockService:
        def get_usd_conversion(self, amount, currency):
            return amount * Decimal('1.5')

class BusinessLogicTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(country="ARG")
        Payment.objects.create(
            user=self.user,
            local_currency=Payment.LocalCurrency.ARS,
            local_total=1000,
            date=timezone.now() - timedelta(days=1),
            status=Payment.PaymentStatus.REJECTED
        )
        Payment.objects.create(
            user=self.user,
            local_currency=Payment.LocalCurrency.ARS,
            local_total=1000,
            date=timezone.now() - timedelta(days=3),
            status=Payment.PaymentStatus.REJECTED
        )
        Payment.objects.create(
            user=self.user,
            local_currency=Payment.LocalCurrency.ARS,
            local_total=2000,
            date=timezone.now() - timedelta(days=2),
            status=Payment.PaymentStatus.COMPLETED
        )
        Payment.objects.create(
            user=self.user,
            local_currency=Payment.LocalCurrency.ARS,
            local_total=1000,
            date=timezone.now() - timedelta(days=4),
            status=Payment.PaymentStatus.COMPLETED
        )
        Payment.objects.create(
            user=self.user,
            local_currency=Payment.LocalCurrency.ARS,
            local_total=10000,
            date=timezone.now() - timedelta(days=8),
            status=Payment.PaymentStatus.COMPLETED
        )    

    def test_calculate_total_amount(self):
        mock_service = MockService()
        total = calculate_total_amount(self.user, 7, mock_service.get_usd_conversion)
        self.assertEqual(total, 4500)

    def test_get_rejected_payments(self):
        quantity = get_rejected_payments(self.user, 2)
        self.assertEqual(quantity, 1)

    
