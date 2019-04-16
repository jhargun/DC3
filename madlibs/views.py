from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import form1
# Create your views here.

def home(request):
    return HttpResponse("Test")

def madlib(request, num):
    #return render(request, 'madlibs/form1.html')
    if request.method == 'POST':
        if num == 1:
            form = form1(request.POST)
            if form.is_valid():
                #Made for loop to clean data and add to context
                context = {}
                vars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
                for i in range(len(vars)):
                    context[vars[i]] = form.cleaned_data[vars[i]]
                return HttpResponse(context)
                #return render(request, 'madlibs/form1.html', context)
            return HttpResponse('Error! Form not valid!')
        return HttpResponse('Not a valid madlib number! Valid numbers: 1')
    else:
        if num == 1:
            form = form1()
        else:
            return HttpResponse('Not a valid madlib number! Valid numbers: 1')
    return render(request, 'madlibs/Form.html', {'form': form})
