# Generated by Django 4.1.13 on 2024-01-25 20:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Купон', 'verbose_name_plural': 'Купоны'},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Процент скидки'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(verbose_name='Начало действия'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(verbose_name='Конец действия'),
        ),
    ]
