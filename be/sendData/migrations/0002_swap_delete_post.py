# Generated by Django 5.1.1 on 2024-12-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_ticker', models.CharField(max_length=10)),
                ('trade_ticker', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
