from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class class_page1(TemplateView):
    template_name = 'third_task/main3.html'


class class_page2(TemplateView):
    template_name = 'third_task/page2_3.html'


class class_page3(TemplateView):
    template_name = 'third_task/page3_3.html'