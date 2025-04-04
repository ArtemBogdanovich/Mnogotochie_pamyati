from django.shortcuts import render

def main(request):
    return render(request, 'app1/index.html')

def about(request):
    return render(request, 'app1/about.html')

def ya(request):
    return render(request, 'app1/ya.html')



