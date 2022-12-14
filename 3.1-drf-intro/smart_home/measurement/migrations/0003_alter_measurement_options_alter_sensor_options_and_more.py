# Generated by Django 4.1.2 on 2022-10-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_sensor_options_remove_measurement_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Показатели датчика'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
