from django.contrib import admin
from payment_module.models import PaymentGateway


# Register your models here.
class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ["token", "balance", "expiry_date", "is_active"]

    class Meta:
        model = PaymentGateway


admin.site.register(PaymentGateway, PaymentGatewayAdmin)


# admin.site.reg
