# Generated by Django 3.0.2 on 2020-02-23 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200223_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='default-food.jpg', upload_to='post_pics'),
        ),
    ]
