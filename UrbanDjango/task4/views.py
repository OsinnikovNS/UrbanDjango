# from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
def main4(request):
    return render(request, 'fourth_task/main4.html')

def page2(request):
    return render(request, 'fourth_task/page2.html')

def page3(request):
    return render(request, 'fourth_task/page3.html')
