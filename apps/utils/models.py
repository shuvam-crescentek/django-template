from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
