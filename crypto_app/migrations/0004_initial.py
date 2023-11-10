# Generated by Django 4.2.3 on 2023-11-04 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crypto_app", "0003_delete_detail"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefgh12345",
                        length=10,
                        max_length=20,
                        prefix="cat",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(default="Fresh Pear", max_length=100)),
                (
                    "invested_amount",
                    models.DecimalField(
                        decimal_places=2, default="0.99", max_digits=9999999999
                    ),
                ),
                (
                    "invested_return",
                    models.DecimalField(
                        decimal_places=2, default="1.99", max_digits=9999999999
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        blank=True, default="normal", max_length=100, null=True
                    ),
                ),
                ("featured", models.BooleanField(default=False)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[
                            ("not processed", "Not Processed"),
                            ("processing", "Processing"),
                            ("paid", "Paid"),
                        ],
                        default="in_review",
                        max_length=16,
                    ),
                ),
                (
                    "sku",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="1234567890",
                        length=10,
                        max_length=20,
                        prefix="plan",
                        unique=True,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
    ]
