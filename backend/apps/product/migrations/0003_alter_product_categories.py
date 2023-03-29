# Generated by Django 4.1.7 on 2023-03-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(db_table='product_categories', related_name='products', to='product.category'),
        ),
    ]
