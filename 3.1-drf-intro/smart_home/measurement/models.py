from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    ordering = ['name']

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = verbose_name + 'и'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    sensor_reading = models.IntegerField()
    create_at= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    class Meta:
        verbose_name ='Показатели датчика'
