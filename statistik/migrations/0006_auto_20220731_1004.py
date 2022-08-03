# Generated by Django 3.2 on 2022-07-31 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistik', '0005_alter_dataperkampung_puskesmas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataperkampung',
            name='kampung_id',
        ),
        migrations.AddField(
            model_name='dataperkampung',
            name='nama_kampung',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='KampungData',
        ),
    ]
