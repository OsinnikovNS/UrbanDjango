from django.contrib import admin
from django.urls import path
from task2.views import class_template, func_template
from task3.views import page1, page2, page3

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', page1.as_view()),
    path('page2/', page2.as_view()),
    path('page3/', page3.as_view()),

    path('index1/', class_template.as_view()),
    path('index2/', func_template),
]
