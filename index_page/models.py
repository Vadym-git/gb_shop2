from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Product Name', max_length=150, blank=False)
    description = models.TextField(verbose_name='Product description', blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ManyToManyField(ProductCategory, verbose_name='Product categories')
    name = models.CharField(verbose_name='Product Name', max_length=150, blank=False)
    description = models.TextField(verbose_name='Product description', blank=True)
    price = models.DecimalField(verbose_name='Product price', max_digits=9, decimal_places=2)

    def get_absolute_url(self):
        return f'/item/{self.id}/'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
