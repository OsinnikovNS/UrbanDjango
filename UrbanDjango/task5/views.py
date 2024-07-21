from django.http import HttpResponse
from django.shortcuts import render
# from .forms import UserRegistrationForm
# from .forms import ContactForm

# def sign_up_by_django(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
    #     if form.is_valid():
    #         # Обработка данных формы
    #         name = form.cleaned_data['first-name']
    #         name2 = form.cleaned_data['last-name']
    #         email = form.cleaned_data['email']
    #         age = form.cleaned_data['age']
    #         subscribe = form.cleaned_data['subscribe']
    #
    # else:
    #     form = ContactForm()
    # return render(request, 'fifth_task/registration_page.html')

# Метод HTML
def registration_page(request):
    return render(request, 'fifth_task/registration_page.html')

def reg_page(request):
    return render(request, 'fifth_task/reg_page.html')