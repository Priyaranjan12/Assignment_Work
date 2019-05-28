from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    return render(request, 'home.html')


def fibosr(request):

       try:
        mynum = int(request.GET['num'])
        n= int(request.GET['n'])
        myarr = []
        a = 1
        b = 1

        myarr.append(a)
        if mynum != 1:
            myarr.append(b)

        for i in range(1, mynum - 1):
            c = a + b
            a = b
            b = c
            myarr.append(c)
        arrlist = myarr
        arrlist[n - 1]
        return render(request,"result.html", {'result': arrlist[n-1]})


       except Exception as e:

            msg = 'You have entered a index number which is more than the array size that you want to acces'

            return HttpResponse(msg)