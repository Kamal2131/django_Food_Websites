from django.shortcuts import render

# Create your views here.
from .models import food
def foodMenu(request):
    c = food.objects.all()
    return render(request,"food\idex.html",{'d':c})