from my_dj.upload_app.views import upload_view
from django.urls import path

app_name = "upload_app"

urlpatterns = [
    path("upload/", upload_view, name="upload"),
]
