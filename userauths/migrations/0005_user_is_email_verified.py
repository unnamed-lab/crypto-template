# Generated by Django 4.2.3 on 2023-11-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0004_user_payment_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_email_verified",
            field=models.BooleanField(default=False),
        ),
    ]