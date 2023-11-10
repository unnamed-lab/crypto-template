from django.urls import path
from .views import index, dashboard_view, profile_view, profile_settings_view, coin_detail_view, coin_list_view, payment_view

app_name = "core"

urlpatterns = [
    path('', index, name='index'),
    path('app/coins/', coin_list_view, name='coin-list'),
    path('app/coin/<pid>/', coin_detail_view, name='coin-detail'),
    path('app/dashboard', dashboard_view, name='dashboard'),
    path('app/profile', profile_view, name='profile'),
    path('app/profile-settings', profile_settings_view, name='profile-settings'),
    path('app/coin/payment', payment_view, name='payment'),
]
