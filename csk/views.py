from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name':'MSD','age':43,'team':'Chennai Super Kings'}
    return render(request,'ipl.html',context=d)