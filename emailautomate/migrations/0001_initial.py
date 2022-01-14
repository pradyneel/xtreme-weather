# Generated by Django 3.1.6 on 2022-01-14 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('city', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Chennai', 'Chennai'), ('Bangalore', 'Bangalore'), ('Kolkata', 'Kolkata')], default='Chennai', max_length=20)),
                ('timeOfSendingMail', models.DateTimeField(default=datetime.datetime(2022, 1, 14, 11, 32, 13, 16399))),
            ],
        ),
    ]