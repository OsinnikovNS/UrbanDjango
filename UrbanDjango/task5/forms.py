# from django import forms
# from django.contrib.auth.models import User

# представление для  регистрации пользователей на нашем сайте
# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'email')
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']



# class ContactForm(forms.Form):
#     name = forms.CharField(max_lenght=25, lable='Введите Фамилию:')
#     name2 = forms.CharField(max_lenght=25, lable='Введите Имя:')
#     email = forms.EmailField(lable='Email')
#     age = forms.CharField(max_lenght=3, lable='Введите свой возраст (количество лет):')
#     subscribe = forms.BooleanField(required=False, lable='Я принимаю условия и положения')