# Generated by Django 3.1.14 on 2022-05-31 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0019_auto_20220531_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='avance',
            name='fouration_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud.fourations'),
        ),
    ]
