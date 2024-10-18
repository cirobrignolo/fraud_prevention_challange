from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import FraudCheckSerializer
from .business_logic import get_rejected_payments, calculate_total_amount

@api_view(['GET'])
def fraud_check(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
    
    # Select the number of days for each function; since it is fixed, it does not work as an input parameter.
    days_for_rejected_payments = 1
    days_for_total_amt = 7

    data = {
        "is_new_user": user.is_new(),
        "qty_rejected_1d": get_rejected_payments(user, days_for_rejected_payments),
        "total_amt_7d": calculate_total_amount(user, days_for_total_amt)
    }

    serializer = FraudCheckSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data)
