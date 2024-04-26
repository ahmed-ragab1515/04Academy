# Generated by Django 4.2.11 on 2024-04-25 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuitableTiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=50, verbose_name='التوقيت المناسب')),
            ],
            options={
                'verbose_name_plural': '11_suitable_timing',
            },
        ),
        migrations.AlterField(
            model_name='studyschedule',
            name='suitable_timing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.suitabletiming', verbose_name='التوقيت المناسب'),
        ),
    ]
