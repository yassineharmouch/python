# Generated by Django 4.0.4 on 2022-05-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255)),
                ('search', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=10)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CsvUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('end_date', models.DateTimeField()),
                ('notes', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fourations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_tir', models.CharField(choices=[('nonel', 'nonel'), ('electrique', 'electrique'), ('classique', 'classique')], max_length=150)),
                ('type_tir', models.CharField(choices=[('42ms,25ms,17ms', '42ms,25ms,17ms'), ('42ms,17ms', '42ms,17ms')], max_length=150)),
                ('mode_charge', models.CharField(choices=[('unique', 'unique'), ('etag??', '??tag??')], max_length=150)),
                ('niveau', models.CharField(choices=[('RT/SB', 'RT/SB'), ('RT/SA2', 'RT/SA2'), ('INT1/2', 'INT1/2'), ('INT2/4', 'INT2/4'), ('INT3/4', 'INT3/4'), ('INT3/5', 'INT3/5'), ('INT5/6', 'INT5/6'), ('INT4/5', 'INT4/5'), ('INT2/3', 'INT2/3'), ('INTSA2/C0', 'INTSA2/C0'), ('RT/C0', 'RT/C0'), ('RT/C2', 'RT/C2'), ('RT/C3', 'RT/C3'), ('RT/C4', 'RT/C4'), ('RT/C5', 'RT/C5')], max_length=150)),
                ('panneau', models.CharField(choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7'), ('P8', 'P8')], max_length=150)),
                ('largeur', models.CharField(max_length=255)),
                ('nbr_trou_range', models.CharField(max_length=255)),
                ('tranche', models.CharField(max_length=255)),
                ('profondeur', models.CharField(max_length=255)),
                ('dossage', models.CharField(max_length=255)),
                ('nbr_trou', models.CharField(max_length=255)),
                ('maille', models.CharField(max_length=255)),
                ('longueur', models.CharField(max_length=50)),
                ('nbr_range', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('mobile_number', models.CharField(blank=True, max_length=10)),
                ('description', models.TextField(max_length=255)),
                ('location', models.TextField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=150)),
                ('date', models.DateField(verbose_name='%m/%d/%Y')),
                ('created_at', models.DateTimeField(verbose_name='%m/%d/%Y %H:%M:%S')),
                ('updated_at', models.DateTimeField(verbose_name='%m/%d/%Y %H:%M:%S')),
            ],
        ),
        migrations.CreateModel(
            name='Sautage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_tir', models.CharField(choices=[('42ms,25ms,17ms', '42ms,25ms,17ms'), ('42ms,17ms', '42ms,17ms')], max_length=150)),
                ('case_debut', models.CharField(max_length=255)),
                ('equipe', models.CharField(max_length=255)),
                ('son', models.CharField(max_length=255)),
                ('frequence', models.CharField(max_length=255)),
                ('vitesse', models.CharField(max_length=255)),
                ('vitesse_vent', models.CharField(max_length=255)),
                ('humiditer', models.CharField(max_length=255)),
                ('temp', models.CharField(max_length=255)),
                ('taux_abattage', models.CharField(max_length=255)),
                ('taux_deplacement', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
