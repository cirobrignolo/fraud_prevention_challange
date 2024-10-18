from django.utils import timezone
from django.db import models
import uuid

class User(models.Model):
    class Countries(models.TextChoices):
        ARG = 'ARG', 'Argentina'
        URU = 'URU', 'Uruguay'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(
        max_length=3,
        choices=Countries.choices,
        default=Countries.ARG,
        null=False,
        blank=False
    )

    def is_new(self):
        return (timezone.now() - self.created_at).days < 7

class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        COMPLETED = 'completed', 'Completed'
        REJECTED = 'rejected', 'Rejected'

    class LocalCurrency(models.TextChoices):
        ARS = 'ARS', 'Argentine Pesos'
        UYU = 'UYU', 'Uruguayan Pesos'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    local_currency = models.CharField(
        max_length=3,
        choices=LocalCurrency.choices,
        default=LocalCurrency.ARS,
        null=False,
        blank=False
    )
    local_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)
    status = models.CharField(
        max_length=20, 
        choices=PaymentStatus.choices,
        default=PaymentStatus.COMPLETED,
        null=False,
        blank=False
    )
