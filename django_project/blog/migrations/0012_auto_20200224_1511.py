# Generated by Django 3.0.2 on 2020-02-24 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200224_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imgfood',
            new_name='image',
        ),
    ]
