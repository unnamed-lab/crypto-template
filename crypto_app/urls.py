from django.urls import path
from .views import index, dashboard_view, profile_view, profile_settings_view, coin_detail_view, coin_list_view, payment_view, send_payment_review,custom_error_404_view,custom_error_500_view

app_name = "core"

urlpatterns = [
    path('', index, name='index'),
    path('app/coins/', coin_list_view, name='coin-list'),
    path('app/coin/<pid>/', coin_detail_view, name='coin-detail'),
    path('app/dashboard', dashboard_view, name='dashboard'),
    path('app/profile', profile_view, name='profile'),
    path("send-payment-review/<pid>/", send_payment_review, name="send-payment-review"),
    path('app/profile-settings', profile_settings_view, name='profile-settings'),
    path('app/coin/payment', payment_view, name='payment'),
]
handler500 = custom_error_500_view
handler404 = custom_error_404_view