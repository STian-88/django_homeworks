from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='МОДЕЛЬ')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость')
    image = models.TextField(verbose_name='МОДЕЛЬ')
    release_date = models.CharField(max_length=15, verbose_name='ДАТА РЕЛИЗА')
    lte_exists = models.BooleanField(verbose_name='LTE')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)


