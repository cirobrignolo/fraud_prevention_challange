from decimal import Decimal
from django.test import TestCase
from api.serializers import FraudCheckSerializer

class FraudCheckSerializerTests(TestCase):
    def test_valid_serializer(self):
        data = {
            "is_new_user": True,
            "qty_rejected_1d": 0,
            "total_amt_7d": Decimal('100.00')
        }
        serializer = FraudCheckSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['is_new_user'], True)
        self.assertEqual(serializer.validated_data['qty_rejected_1d'], 0)
        self.assertEqual(serializer.validated_data['total_amt_7d'], Decimal('100.00'))

    def test_invalid_serializer_missing_field(self):
        data = {
            "qty_rejected_1d": 0,
            "total_amt_7d": Decimal('100.00')
        }
        serializer = FraudCheckSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('is_new_user', serializer.errors)

    def test_invalid_serializer_invalid_data(self):
        data = {
            "is_new_user": "not_a_boolean",
            "qty_rejected_1d": -1,
            "total_amt_7d": "not_a_decimal"
        }
        serializer = FraudCheckSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('is_new_user', serializer.errors)
        self.assertIn('qty_rejected_1d', serializer.errors)
        self.assertIn('total_amt_7d', serializer.errors)
