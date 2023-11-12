# Generated by Django 4.2.3 on 2023-11-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0011_alter_user_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="total_balance",
            field=models.DecimalField(
                decimal_places=2, default="0.00", max_digits=99999
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="total_invested",
            field=models.DecimalField(
                decimal_places=2, default="0.00", max_digits=99999
            ),
        ),
    ]