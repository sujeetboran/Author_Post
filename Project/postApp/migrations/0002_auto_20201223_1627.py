# Generated by Django 3.1.1 on 2020-12-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
