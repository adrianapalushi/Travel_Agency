# Generated by Django 4.0.3 on 2022-03-27 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_alter_airport_options_alter_continent_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_departure', models.DateTimeField()),
                ('date_of_return', models.DateTimeField()),
                ('number_of_days', models.IntegerField()),
                ('trip_type', models.CharField(choices=[('BB', 'Bed & Breakfast'), ('HB', 'Half Board'), ('FB', 'Full Board'), ('AI', 'All Inclusive')], max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('price_for_adult', models.FloatField(blank=True, null=True)),
                ('price_for_child', models.FloatField(blank=True, null=True)),
                ('promoted', models.BooleanField(default=False)),
                ('number_of_adults', models.IntegerField(default=0)),
                ('number_of_children', models.IntegerField(default=0)),
                ('from_airport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_trips', to='trips.airport')),
                ('from_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_trips', to='trips.city')),
                ('to_airport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_trips', to='trips.airport')),
                ('to_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_trips', to='trips.city')),
                ('to_hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_trips', to='trips.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_adults', models.IntegerField()),
                ('number_of_children', models.IntegerField()),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip')),
            ],
        ),
    ]