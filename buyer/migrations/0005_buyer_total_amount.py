# Generated by Django 5.1.6 on 2025-03-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_buyer_product_names_buyer_total_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
