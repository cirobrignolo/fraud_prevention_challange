from rest_framework import serializers

class FraudCheckSerializer(serializers.Serializer):
    is_new_user = serializers.BooleanField()
    qty_rejected_1d = serializers.IntegerField()
    total_amt_7d = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_qty_rejected_1d(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity of rejected payments cannot be negative.")
        return value
    
    def validate_total_amt_7d(self, value):
        if value < 0:
            raise serializers.ValidationError("Total amount cannot be negative.")
        return value
    