from django.shortcuts import render




# Create your views here.
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
import jinja2
import math

# Create your views here.
def bpCalc(s):
    s = s
    r = int(s)
    c = 132860
    n = 1
    #for n in range(1, (r - 2)):
    while n < (r-1):
        c = c * (365 - (n + 1))
        n = n + 1
    a = (1 - (c / (365 ** r)))
    return '%30.2f' %(round(a, 4)*100)
    

def wrapit(request):
    if request.method == 'POST':
        s = request.POST.get('students')
    dog = bpCalc(s)
    c = {'result': dog}
    temp = loader.get_template('answer.html')
    return HttpResponse(temp.render(c, request))


def calculate(request):
    b = 'enter'
    c = {'tit': b}
    temp = loader.get_template('calculate.html')
    return HttpResponse(temp.render(c, request))

    
     
