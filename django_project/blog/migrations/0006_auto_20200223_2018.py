# Generated by Django 3.0.2 on 2020-02-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200223_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
    ]
