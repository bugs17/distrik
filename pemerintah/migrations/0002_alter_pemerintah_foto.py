# Generated by Django 3.2 on 2022-07-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemerintah', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemerintah',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
