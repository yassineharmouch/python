# Generated by Django 3.1.14 on 2022-05-30 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_auto_20220527_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='fourations',
            name='num_com',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
