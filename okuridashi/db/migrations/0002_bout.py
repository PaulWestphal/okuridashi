# Generated by Django 4.0 on 2022-01-01 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kimarite', models.CharField(max_length=200)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.tournamentday')),
                ('east', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rikishi_east', to='db.rikishi')),
                ('west', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rikishi_west', to='db.rikishi')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='db.rikishi')),
            ],
        ),
    ]
