# Generated by Django 5.1.1 on 2024-09-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_remove_payment_checkout_request_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='checkout_request_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
