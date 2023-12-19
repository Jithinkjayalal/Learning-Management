from django.shortcuts import render

# Create your views here.
from .models import Video
# Create your views here.
def indexs(request):
    video=Video.objects.all()
    return render(request,"indexs.html",{"video":video})