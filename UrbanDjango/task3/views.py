from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class page1(TemplateView):
    template_name = 'third_task/main.html'


class page2(TemplateView):
    template_name = 'third_task/page2.html'


class page3(TemplateView):
    template_name = 'third_task/page3.html'