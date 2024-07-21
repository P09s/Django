from django.shortcuts import render

# Create your views here.
def indexV(request):
    return render(request,"index.html")