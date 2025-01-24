import os
from django.shortcuts import render
form my_dj.settings import BASE_DIR

# Create your views here.
def unload_view(request):
    if request.method == "GET":
        return render(request, "unload_file.html")
    if request.method == "POST":
        upload_obj = request.FILES.get("my_file")
        path = os.path.join(BASE_DIR, "unload_files", upload_obj.name)
        with open(path, "wb") as f:
            for chunk in upload_obj.chunks():
                f.write(chunk)

        data = {
            "msg": "上传成功"
        }
        return JsonResponse(data)