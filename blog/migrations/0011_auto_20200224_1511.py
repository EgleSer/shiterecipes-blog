# Generated by Django 3.0.2 on 2020-02-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200224_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
        migrations.AddField(
            model_name='post',
            name='imgfood',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
