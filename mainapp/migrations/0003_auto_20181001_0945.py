# Generated by Django 2.1.1 on 2018-10-01 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20181001_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labprotocol',
            name='analyst',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
