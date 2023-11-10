from .BaseModel import BaseModel
from django.db import models
from .Category import Category

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL()) # need repair
    image = models.URLField(max_length=255)


    def __str__(self):
        return self.name