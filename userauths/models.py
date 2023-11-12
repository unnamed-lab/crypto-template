from django.db import models
from django.contrib.auth.models import AbstractUser
STATUS_CHOICE = (
    ("not processed", "Not Processed"),
    ("processing", "Processing"),
    ("paid", "Paid"),
)

class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=100)
    total_balance = models.DecimalField(max_digits=99999, decimal_places=2, default="0.00")
    total_invested = models.DecimalField(max_digits=99999, decimal_places=2, default="0.00")
    total_coins = models.IntegerField(default="0")

    contact = models.CharField(max_length=20, blank=True)
    payment_status = models.CharField(max_length=50, choices=STATUS_CHOICE, default="not processing")
    address = models.CharField(max_length=100, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
