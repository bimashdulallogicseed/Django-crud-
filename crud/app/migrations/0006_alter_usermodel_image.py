# Generated by Django 5.0.6 on 2024-07-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_stock_usermodel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(default='', upload_to='static/images/'),
        ),
    ]
