# Generated by Django 3.1 on 2020-08-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, default='Product.jpg', null=True, upload_to=''),
        ),
    ]
