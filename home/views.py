from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def placements(request):
    return render(request, "placements.html")

def about(request):
    return render(request, "about.html")

def myprofile(request):
    return render(request, "myprofile.html")




