# Generated by Django 3.1.4 on 2021-01-19 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20210117_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='stocks.stock'),
        ),
    ]
