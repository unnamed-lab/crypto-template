# Generated by Django 4.2.3 on 2023-11-04 23:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crypto_app", "0005_coin_product_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coin",
            name="title",
            field=models.CharField(default="Bitcoin", max_length=100),
        ),
    ]