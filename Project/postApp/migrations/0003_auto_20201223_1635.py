# Generated by Django 3.1.1 on 2020-12-23 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0002_auto_20201223_1627'),
    ]

    operations = [
        migrations.DeleteModel(
            name='authors',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
