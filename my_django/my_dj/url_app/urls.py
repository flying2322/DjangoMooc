from django import path

from my_dj.url_app.views import go_reverse

app_name = "url"

urlpatterns = [
    path("reverse/", go_reverse, name="reverse"),
    path("hello/", get_url, name="hello"),
    path("show/<fruit>/<sport>/", show_hobby, name="show"),
    path("view/", get_reverse, name="view"),
    path("register/", register_view, name="register")
]