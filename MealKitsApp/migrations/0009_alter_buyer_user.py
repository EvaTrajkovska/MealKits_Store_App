# Generated by Django 4.1.7 on 2023-06-24 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MealKitsApp', '0008_alter_buyer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
