from django.contrib import admin
from crypto_app.models import Category, Coin, UserPaymentReview

class CoinAdmin(admin.ModelAdmin):
    list_display = ['user','title','payment_status','invested_amount', 'invested_return']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cid','title','image']

class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'invested_amount', 'payment_status']
    list_filter = ['payment_status']
    actions = ['confirm_payment']

    def confirm_payment(self, request, queryset):
        # Custom action to manually confirm selected orders
        queryset.update(payment_status=True)

    confirm_payment.short_description = 'Confirm selected orders'

admin.site.register(UserPaymentReview,UserPaymentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Coin, CoinAdmin)


