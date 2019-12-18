from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def response(request):
    return HttpResponse("<h1>Welcome to HttpResponse</h1>")


def  html_demo1(request):
    fruits={'fruit_name':["apple","banana","orange","pinapple"]}
    return render(request,"sample.html",context=fruits)


def  html_demo2(request):
    d={'data':"Django"}
    return render(request,"sample1.html",context=d)