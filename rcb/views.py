from django.shortcuts import render

# Create your views here.
def virat(request):
    d={'name':'Virat Kohli','age':38,'team':'Royal Challengers Banglore'}
    return render(request,'ipl1.html',context=d)