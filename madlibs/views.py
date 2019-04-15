from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Test")

def madlib(request, num):
    return render(request, 'madlibs/form1.html')
    '''if request.method == 'Post':
        if num == 1:
            form = form1(request.POST)
            if form.is_valid():'''
