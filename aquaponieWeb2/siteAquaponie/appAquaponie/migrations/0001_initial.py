# Generated by Django 5.0.3 on 2024-03-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mesure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidite', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ph', models.DecimalField(decimal_places=2, max_digits=5)),
                ('niveauDeau', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lumiere', models.IntegerField()),
            ],
        ),
    ]
