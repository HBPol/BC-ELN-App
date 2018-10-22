# Generated by Django 2.1.1 on 2018-10-01 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0004_sampleanalysis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serial_no', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('calibration_freq_months', models.IntegerField()),
                ('last_calibration_date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('used_in', models.ManyToManyField(to='mainapp.LabProtocol')),
            ],
        ),
        migrations.CreateModel(
            name='Reagents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lot_no', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('expiry_date', models.DateTimeField()),
                ('used_in', models.ManyToManyField(to='mainapp.LabProtocol')),
            ],
        ),
        migrations.AddField(
            model_name='sampleanalysis',
            name='status',
            field=models.CharField(choices=[('REQ', 'Requested'), ('INP', 'In progress'), ('REJ', 'Rejected'), ('ONH', 'On hold'), ('APP', 'Approved')], default='', max_length=3),
        ),
    ]
