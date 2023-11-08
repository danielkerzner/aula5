# Generated by Django 3.2.7 on 2021-10-29 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='movies.movie')),
                ('service', models.CharField(blank=True, max_length=255)),
                ('has_flat_price', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]