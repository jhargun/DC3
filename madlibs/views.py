from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import form1
# Create your views here.

def home(request):
    return render(request, 'madlibs/Home.html')

def madlib(request, num):
    if request.method == 'POST':
        if num == 1:
            form = form1(request.POST)
        elif num == 2:
            form = form2(request.POST)
        if form.is_valid():
            #Made a for loop to clean data and add to context, works since both templates have 10 inputs
            vars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            context = {'j': form.cleaned_data['j']}
            for i in range(len(vars) - 1):
                context[vars[i]] = form.cleaned_data[vars[i]]
            if num == 1:
                return render(request, 'madlibs/lib1.html', context)
            return render(request, 'madlibs/lib2.html', context)
    else:
        if num == 1:
            form = form1()
        elif num == 2:
            form = form2()
        else:
            return HttpResponse('Not a valid madlib number! Valid numbers: 1, 2')
    return render(request, 'madlibs/Form.html', {'form': form})
