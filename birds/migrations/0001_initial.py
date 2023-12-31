# Generated by Django 4.2.6 on 2023-10-31 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название птицы')),
                ('color_feather', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название птицы')),
                ('image_bird', models.ImageField(blank=True, null=True, upload_to='image')),
            ],
            options={
                'verbose_name': 'Птица',
                'verbose_name_plural': 'Птицы',
            },
        ),
    ]
