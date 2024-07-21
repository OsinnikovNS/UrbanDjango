from django.contrib import admin
from django.urls import path
from task2.views import class_template, func_template
from task3.views import class_page1, class_page2, class_page3
from task4.views import main4, page2, page3
from task5.views import registration_page, reg_page

urlpatterns = [
    # path('admin/', admin.site.urls),
# task5
    path('', registration_page),
    path('reg_page', reg_page),
# task4
    path('main4/', main4),
    path('page2/', page2),
    path('page3/', page3),
# task3
    path('main3/', class_page1.as_view()),
    path('page2_3/', class_page2.as_view()),
    path('page3_3/', class_page3.as_view()),
# task2
    path('index1/', class_template.as_view()),
    path('index2/', func_template),
]
