from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def my_post(request):
    return render(request, 'myPost.html')