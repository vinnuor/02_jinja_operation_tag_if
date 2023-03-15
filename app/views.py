from django.shortcuts import render

# Create your views here.
def sample_if(request):
    d={'a':'20','b':'50'}
    return render(request,'sample_if.html',d)