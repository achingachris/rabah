# Generated by Django 4.2.7 on 2023-12-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabah_subscriptions', '0003_rename_is_completed_billingaddress_is_billing_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='is_card_verified',
            field=models.BooleanField(default=False),
        ),
    ]
