# Generated by Django 2.2.1 on 2019-06-02 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('everton', '0008_playertransfers_visible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playertransfers',
            old_name='playername',
            new_name='name',
        ),
    ]
