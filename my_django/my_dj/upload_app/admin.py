from django.contrib import admin

# Register your models here.
from my_dj.upload_app.models import Fruits

models = [
    Fruits,
]

admin.site.register(models)