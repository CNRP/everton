# Generated by Django 2.2.1 on 2019-06-02 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everton', '0006_playertransfers'),
    ]

    operations = [
        migrations.AddField(
            model_name='playertransfers',
            name='position',
            field=models.CharField(default='CM', max_length=400),
        ),
    ]
