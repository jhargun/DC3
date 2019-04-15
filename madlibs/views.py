from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Test")

def madlib(request, num):
    #return render(request, 'madlibs/form1.html')
    if request.method == 'Post':
        if num == 1:
            form = form1(request.POST)
            if form.is_valid():
                #Made for loop to clean data and add to context
                context = {}
                vars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
                for i in range(len(vars)):
                    context[vars[i]] = form.cleaned_data[vars[i]]
                return render(request, 'madlibs/form1.html', context)
    else:
        if num == 1:
            form = form1()
            context = {'form': form,
                       'page': reverse('madlibs:madlib', args=(num))}
            return render(request, 'madlibs/Form.html',)
