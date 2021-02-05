from django.shortcuts import render
from Pythonproject.models import userinfo

def function(request):
    key = userinfo.objects.all()
    return render(request,'index.html',{'value':key})
def page2(request):
    return (request,'index2')
