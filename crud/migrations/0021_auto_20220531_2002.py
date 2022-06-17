# Generated by Django 3.1.14 on 2022-05-31 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0020_avance_fouration_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fourations',
            name='stock_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud.stock'),
        ),
        migrations.AddField(
            model_name='stock',
            name='num_stock',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]