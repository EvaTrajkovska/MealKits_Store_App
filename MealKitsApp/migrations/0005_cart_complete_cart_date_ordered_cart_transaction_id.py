# Generated by Django 4.1.7 on 2023-06-23 11:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MealKitsApp', '0004_alter_menu_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
