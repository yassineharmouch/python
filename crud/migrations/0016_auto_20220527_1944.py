# Generated by Django 3.1.14 on 2022-05-27 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0015_sautage_num_com'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sautage',
            old_name='num_com',
            new_name='fouration_id',
        ),
    ]
