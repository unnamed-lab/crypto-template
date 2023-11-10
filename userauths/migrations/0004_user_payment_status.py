# Generated by Django 4.2.3 on 2023-11-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0003_user_private_key_user_public_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("not processed", "Not Processed"),
                    ("processing", "Processing"),
                    ("paid", "Paid"),
                ],
                default="not processing",
                max_length=50,
            ),
        ),
    ]