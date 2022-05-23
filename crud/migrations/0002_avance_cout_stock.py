# Generated by Django 4.0.4 on 2022-05-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avance_foration', models.CharField(max_length=255)),
                ('avance_sautage', models.CharField(max_length=255)),
                ('avance_actuel', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammonix', models.CharField(max_length=255)),
                ('tovex', models.CharField(max_length=255)),
                ('raccord17ms', models.CharField(max_length=255)),
                ('raccord25ms', models.CharField(max_length=255)),
                ('raccord42ms', models.CharField(max_length=255)),
                ('cout_global', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammonix', models.CharField(max_length=255)),
                ('tovex', models.CharField(max_length=255)),
                ('raccord17ms', models.CharField(max_length=255)),
                ('raccord25ms', models.CharField(max_length=255)),
                ('raccord42ms', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]