# Generated by Django 3.1.1 on 2020-12-23 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authors',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=10)),
                ('posts', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('views', models.IntegerField(default=0)),
                ('reviews', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postApp.authors')),
            ],
        ),
    ]
