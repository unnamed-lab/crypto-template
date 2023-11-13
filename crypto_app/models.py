from django.db import models
from shortuuid.django_fields import ShortUUIDField
from userauths.models import User
from django.utils.html import mark_safe
STATUS_CHOICE = (
    ("not processed", "Not Processed"),
    ("processing", "Processing"),
    ("paid", "Paid"),
)
STATUS = (
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345") #custom uuid field
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.title
class Coin(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345") #product uuid field
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="Bitcoin")
    description = models.TextField(null=True, blank=True)
    initial = models.CharField(max_length=7, default="BTC")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    invested_amount = models.DecimalField(max_digits=1000, decimal_places=2, default="0.99")
    invested_return = models.DecimalField(max_digits=1000, decimal_places=2, default="1.99")
    type = models.CharField(max_length=100, default="normal", null=True, blank=True)
    featured = models.BooleanField(default=False)
    payment_status = models.CharField(choices=STATUS_CHOICE, max_length=16, default="in_review")
    sku = ShortUUIDField(unique=True, length=10, max_length=20, prefix="plan", alphabet="1234567890") 
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    class Meta:
        verbose_name_plural = "Coins"

    def __str__(self):
        return self.title
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def get_percentage(self):
        profit = (self.invested_amount/self.invested_return) * 100
        return profit

class UserPaymentReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Bitcoin")
    initial = models.CharField(max_length=7, default="BTC")
    invested_amount = models.DecimalField(max_digits=1000, decimal_places=2, default="0")
    invested_return = models.DecimalField(max_digits=1000, decimal_places=2, default="0")
    payment_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    percentage = models.DecimalField(max_digits=999, decimal_places=2, default="0")