from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):  #request argument is going to represent http request that user want to access in web server
    return render(request,"Promoter/index.html")

