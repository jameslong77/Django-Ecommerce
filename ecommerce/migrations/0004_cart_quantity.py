# Generated by Django 2.1.2 on 2018-10-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
