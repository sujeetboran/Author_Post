# Generated by Django 3.1.1 on 2020-12-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0004_authors_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
