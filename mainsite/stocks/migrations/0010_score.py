# Generated by Django 3.1.4 on 2021-06-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_statistics_regular_market_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('game_id', models.IntegerField()),
            ],
        ),
    ]
