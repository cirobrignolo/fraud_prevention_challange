from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import FraudCheckSerializer
from .business_logic import get_rejected_payments, calculate_total_amount
import logging
from rest_framework import status
from django.conf import settings

@api_view(['GET'])
def fraud_check(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    try:
        data = {
            "is_new_user": user.is_new(),
            "qty_rejected_1d": get_rejected_payments(user, settings.DAYS_FOR_REJECTED_PAYMENTS),
            "total_amt_7d": calculate_total_amount(user, settings.DAYS_FOR_TOTAL_AMOUNT)
        }
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logging.error(f"Unexpected error in fraud_check: {e}")
        return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = FraudCheckSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data)
