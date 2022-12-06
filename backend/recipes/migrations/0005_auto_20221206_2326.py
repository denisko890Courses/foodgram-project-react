# Generated by Django 2.2.19 on 2022-12-06 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_add_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное количество: 1')], verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('#E26C2D', 'Оранжевый'), ('#49B64E', 'Зеленый'), ('#8775D2', 'Пурпурный')], max_length=7, unique=True, verbose_name='Цвет в HEX'),
        ),
    ]
