from django import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=64)
    pwd = models.CharField(max_length=128)

    @classmethod
    def create_one(cls,**kwargs):
        cls.objects.create(
            user_name=kwargs.get("user_name"),
            pwd=kwargs.get("pwd")
        )