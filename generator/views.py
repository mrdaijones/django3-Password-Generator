from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    lower = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 16))

    thepassword=''
    for x in range(length):
        thepassword += random.choice(lower)

    if request.GET.get('uppercase'):
        upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        nupper = int(request.GET.get('nupper'))
        #print('Uppercase selected', nupper)
        for x in range(nupper):
            y = random.randint(1, length)
            #print('y=', y)
            lp = list(thepassword)
            #print('lp=', lp)
            lp[y-1] = random.choice(upper)
            #print('lp=', lp)
            thepassword = ''
            for x in range(length):
                thepassword += lp[x]

    if request.GET.get('numbers'):
        numbers = list('0123456789')
        nnum = int(request.GET.get('nnum'))
        for x in range(nnum):
            y = random.randint(1, length)
            lp = list(thepassword)
            lp[y-1] = random.choice(numbers)
            thepassword = ''
            for x in range(length):
                thepassword += lp[x]

    if request.GET.get('special'):
        special = list('@#$%^&*(){}')
        nspecial = int(request.GET.get('nspecial'))
        for x in range(nspecial):
            y = random.randint(1, length)
            lp = list(thepassword)
            lp[y-1] = random.choice(special)
            thepassword = ''
            for x in range(length):
                thepassword += lp[x]

    return render(request, 'generator/password.html', {'password':thepassword})

