from BaseModel import BaseModel
from django.db import models

class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name