# Generated by Django 4.1.7 on 2023-06-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MealKitsApp', '0013_remove_recipe_qty_productportions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productportions',
            name='size',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
    ]
