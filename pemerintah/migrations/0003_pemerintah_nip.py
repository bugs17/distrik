# Generated by Django 3.2 on 2022-07-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemerintah', '0002_alter_pemerintah_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pemerintah',
            name='nip',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
