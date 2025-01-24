from django import render
from django.http import HttpResponse
from django import reverse
# Create your views here.

def go_reverse(request):
    return render(request, "reverse.html")

def get_url(request):
    return render(request, "hello_reverse.html")



def show_hobby(request, fruit, sport):
    msg = f"我喜欢的水果是：{fruit}; 喜欢的运动是：{sport}"
    return HttpResponse(f"<h3>{msg}</h3>")

def get_reverse(request):
    fruit = "Banana"
    sport = "Foot Ball"
    # return redirect(reverse("url:show", args=(fruit, sport))) # 元组传参 元素传参
    return redirect(reverse("url:show", kwargs={"fruit": fruit, "sport": sport})) # 通过字典方式传参 = 关键字传参

def register_view(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        name = request.POST.get("register_name")
        pwd = request.POST.get("register_pwd")
        data = {
            "user_name": name,
            "pwd": pwd
        }
        User.create_one(**data)
        return redirect(reverse(""))
        # User.create_one(**{"user_name":name, "pwd":pwd})
    # return render(request, 'register.html')

def login_view(request):
    if request.method == "GET":
        return render(request, )