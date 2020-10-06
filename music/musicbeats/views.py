from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def sad(request):
     return HttpResponse("sad songs page")

# def musicbeats(request):
#   return render(request,'index1.html')

def musicbeats(a,b):
    if 1==1:
        # c=a+b
        # print("sad")
        return redirect('www.youtube.com')