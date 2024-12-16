# from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    # return HttpResponse("its homepage")
    return render(request, 'home.html')
def about(request):
    # return HttpResponse("its about page")
      return render(request, 'about.html')