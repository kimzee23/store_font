from django.http.response import HttpResponse
from django.shortcuts import render

def something(request):
    return render(request, "hello.html", { "name": "John" })
