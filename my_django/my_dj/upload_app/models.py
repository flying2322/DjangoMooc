from django.db import models

# Create your models here.

class Fruits(models.Model):
    name = models.CharField(max_length=32, verbose_name="水果名称")
