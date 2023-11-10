# Generated by Django 4.2.3 on 2023-11-10 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crypto_app", "0013_coin_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userpaymentreview",
            name="product_status",
        ),
        migrations.AlterField(
            model_name="userpaymentreview",
            name="payment_status",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="userpaymentreview",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
