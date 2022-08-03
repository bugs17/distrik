# Generated by Django 3.2 on 2022-07-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskripsi', models.CharField(max_length=100)),
                ('file', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
    ]