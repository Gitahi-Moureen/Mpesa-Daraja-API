from django.db import models

# Create your models here.
# payments/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True) 
    phone_number = models.CharField(max_length=15, default='0000000000')
    checkout_request_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')  # Default status
    # transaction_id = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment {self.amount} - {self.status}"
