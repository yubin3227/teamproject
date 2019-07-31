from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def guide(request):
    return render(request, 'guide.html')

def synergy(request):
    return render(request, 'synergy.html')

def item(request):
    return render(request, 'item.html')

def url(request):
    return render(request, 'url.html')