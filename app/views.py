from django.shortcuts import render

# Create your views here.

def bg_image(request):
    return render(request,'bg_image.html')


def mdb_bootstrap(request):
    return render(request,'mdb_bootstrap.html')

