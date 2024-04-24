# Generated by Django 5.0.3 on 2024-04-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAquaponie', '0009_cheatsheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datafile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='datafile/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cheatsheet',
        ),
    ]