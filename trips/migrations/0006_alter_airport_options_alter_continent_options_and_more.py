# Generated by Django 4.0.3 on 2022-03-27 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_hotel_airport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airport',
            options={'verbose_name': 'airport', 'verbose_name_plural': 'airports'},
        ),
        migrations.AlterModelOptions(
            name='continent',
            options={'verbose_name': 'continent', 'verbose_name_plural': 'continents'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name': 'hotel', 'verbose_name_plural': 'hotels'},
        ),
    ]