# Generated by Django 3.1.14 on 2022-05-25 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0013_remove_pfourations_dr'),
    ]

    operations = [
        migrations.AddField(
            model_name='pfourations',
            name='densite_r',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
