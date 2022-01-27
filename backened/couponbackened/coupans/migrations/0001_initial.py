# Generated by Django 4.0.1 on 2022-01-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllCoupons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(default='none', max_length=4)),
                ('discountPercent', models.BigIntegerField()),
                ('fixeddiscount', models.CharField(default=0, max_length=3)),
                ('minAmounttouse', models.BigIntegerField()),
            ],
        ),
    ]
