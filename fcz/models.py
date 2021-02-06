from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager 

class Product(models.Model):
    
    STATUS_CHOICE = (
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock')
    )

    name = models.CharField(max_length=500)
    img = models.ImageField()
    price = models.IntegerField()
    slug = models.SlugField()
    brand = models.CharField(blank=True, null=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    warranty = models.TextField(blank=True, null=True)
    tags = TaggableManager()
    upload = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, default='in_stock',\
                                 choices=STATUS_CHOICE)

    class Meta:
        ordering = ('-upload',)

    def get_absolute_url(self):
        return reverse("fcz:product_detail", args=[
            self.upload.day,
            self.upload.month,
            self.upload.year,
            self.slug
        ])
    

    def __str__(self):
        return self.name
    
class Feature(models.Model):
    product = models.ForeignKey(Product, related_name='features',\
                                         on_delete=models.CASCADE)
    ft_name = models.CharField(max_length=250)
    ft_value = models.CharField(max_length=250)

    def __str__(self):
        return self.ft_name
    
class Categorie(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    def __str__(self):
        return self.title
 
