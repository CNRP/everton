# Generated by Django 2.2.1 on 2019-06-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everton', '0007_playertransfers_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='playertransfers',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
