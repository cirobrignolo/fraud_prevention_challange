from datetime import timedelta
from decimal import Decimal
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from api.models import User, Payment

class FraudCheckTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(country="AR")
        self.payment = Payment.objects.create(
            user=self.user,
            local_currency=Payment.LocalCurrency.ARS,
            local_total=1000,
            date=timezone.now() - timedelta(days=4),
            status=Payment.PaymentStatus.COMPLETED
        )

    def test_fraud_check(self):
        url = reverse('fraud-check', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['is_new_user'])
        self.assertEqual(response.data['qty_rejected_1d'], 0)
        self.assertTrue(Decimal(response.data['total_amt_7d']) >= 0)
