# Generated by Django 3.2 on 2022-07-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pemerintah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('golongan', models.CharField(max_length=100)),
                ('jabatan', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='upload/image/')),
            ],
        ),
    ]
