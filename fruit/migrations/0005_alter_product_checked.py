# Generated by Django 5.0.3 on 2024-06-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0004_category_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
