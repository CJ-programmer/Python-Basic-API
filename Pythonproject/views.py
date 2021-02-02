from django.shortcuts import render

def function(request):
    return render(request,'index.html')
def page2(request):
    return render(request,'index2.html',{})   
