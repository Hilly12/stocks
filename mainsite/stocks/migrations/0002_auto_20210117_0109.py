# Generated by Django 3.1.4 on 2021-01-17 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='date',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='company',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='id',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='current_price',
        ),
        migrations.AddField(
            model_name='statistics',
            name='current_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='currency',
            field=models.CharField(default='USD', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statistics',
            name='stock',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stocks.stock'),
        ),
    ]
