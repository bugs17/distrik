# Generated by Django 3.2 on 2022-07-29 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='berita',
            old_name='gamabar',
            new_name='gambar',
        ),
    ]
