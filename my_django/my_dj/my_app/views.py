from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h3 style='color:green'>Hello Django!</h3>")