from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import User, Payment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'country')
    search_fields = ('country',)
    ordering = ('created_at',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'local_currency', 'local_total', 'date', 'status')
    list_filter = ('local_currency', 'status')
    search_fields = ('user__id', 'status')
    ordering = ('date',)

    def save_model(self, request, obj, form, change):
        if not User.objects.filter(id=obj.user.id).exists():
            raise ValidationError(f"The user whit id {obj.user.id} does no exists.")
        super().save_model(request, obj, form, change)
