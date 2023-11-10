from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)  # primary key
    created_at = models.DateTimeField(auto_now_add=True)  # default value set at creation
    updated_at = models.DateTimeField(auto_now=True)  # default value set at every update
    is_deleted = models.BooleanField(default=False)  # soft delete

    class Meta:
        abstract = True
