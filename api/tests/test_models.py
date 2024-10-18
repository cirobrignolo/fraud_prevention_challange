from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from api.models import Payment, User

class UserModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(country="ARG")
        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)

    def test_user_creation_invalid_country(self):
        user = User(country="")
        with self.assertRaises(ValidationError):
            user.full_clean()

class PaymentModelTests(TestCase):
    def test_payment_creation(self):
        user = User.objects.create(country="ARG")
        payment = Payment.objects.create(
            user=user,
            local_currency=Payment.LocalCurrency.ARS,
            local_total=1000,
            date=timezone.now(),
            status=Payment.PaymentStatus.COMPLETED
        )
        self.assertIsInstance(payment, Payment)
        self.assertIsNotNone(payment.id)

    def test_payment_creation_invalid_user(self):
        payment = Payment(
            user=None,
            local_currency=Payment.LocalCurrency.ARS,
            local_total=1000,
            date=timezone.now(),
            status=Payment.PaymentStatus.COMPLETED
        )
        with self.assertRaises(ValidationError):
            payment.full_clean()