# Generated by Django 4.1.7 on 2023-06-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MealKitsApp', '0014_alter_productportions_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='qty',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
        migrations.DeleteModel(
            name='ProductPortions',
        ),
    ]
