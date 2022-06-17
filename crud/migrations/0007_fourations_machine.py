# Generated by Django 4.0.4 on 2022-05-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_remove_fourations_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='fourations',
            name='machine',
            field=models.CharField(choices=[('7500/1', '7500/1'), ('7500/2', '7500/2'), ('PH1', 'PH1'), ('PH2', 'PH2'), ('D11', 'D11'), ('E.E', 'E.E')], default=2, max_length=150),
            preserve_default=False,
        ),
    ]