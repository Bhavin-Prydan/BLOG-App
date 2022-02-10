# Generated by Django 2.2 on 2020-06-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField(max_length=1000)),
                ('timeStemp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]