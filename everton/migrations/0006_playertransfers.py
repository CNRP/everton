# Generated by Django 2.2.1 on 2019-06-02 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everton', '0005_auto_20190526_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerTransfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playername', models.CharField(max_length=80)),
                ('fromclubname', models.CharField(default='Everton', max_length=400)),
                ('fromabervated', models.CharField(default='EFC', max_length=400)),
                ('toclubname', models.CharField(default='Barcelona', max_length=80)),
                ('toabervated', models.CharField(default='BAR', max_length=400)),
                ('type', models.CharField(default='loan', max_length=80)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Player Transfers',
            },
        ),
    ]
