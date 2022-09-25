from cProfile import label
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Elektron poçt ünvanızı daxil edin:',
        widget=forms.TextInput(attrs={'placeholder': 'İstifadəçi adı', 
        'style': 'width: 50%; min-width: 280px;'}),
        error_messages={
            'empty_value': "Boş dəyər daxil edilib.",
            'required': "Bu xana boş ola bilməz.",
            'invalid': "Yalnış dəyər daxil edilib.",
            'max_length': "Simvolların sayı maksimumu keçib.",
            'min_length': "Simvolların sayı minimumun altındadır."
            }
        )

    email = forms.EmailField(
        label='Elektron poçt ünvanızı daxil edin:',
        widget=forms.EmailInput(attrs={'placeholder': 'Elektron poçt ünvanı', 
        'style': 'width: 50%; min-width: 280px;'}),
        error_messages={
            'empty_value': "Boş dəyər daxil edilib.",
            'required': "Bu xana boş ola bilməz.",
            'invalid': "Yalnış dəyər daxil edilib.",
            'max_length': "Simvolların sayı maksimumu keçib.",
            'min_length': "Simvolların sayı minimumun altındadır."
            }
        )

    password1 = forms.CharField(
        label='Şifrənizi daxil edin:',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrə', 
        'style': 'width: 50%; min-width: 280px;'}),
        error_messages={
            'empty_value': "Boş dəyər daxil edilib.",
            'required': "Bu xana boş ola bilməz.",
            'max_length': "Simvolların sayı maksimumu keçib.",
            'min_length': "Simvolların sayı minimumun altındadır."
            }
        )
    password2 = forms.CharField(
        label='Şifrənizi təkrarlayın:',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrə', 
        'style': 'width: 50%; min-width: 280px;'}),
        error_messages={
            'empty_value': "Boş dəyər daxil edilib.",
            'required': "Bu xana boş ola bilməz.",
            'max_length': "Simvolların sayı maksimumu keçib.",
            'min_length': "Simvolların sayı minimumun altındadır."
            }
        )

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
        

class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        label='İstifadəçi adınızı daxil edin:',
        widget=forms.TextInput(attrs={'placeholder': 'İstifadəçi adı', 
        'style': 'width: 50%; min-width: 280px;'}),
        error_messages={
            'empty_value': "Boş dəyər daxil edilib.",
            'required': "Bu xana boş ola bilməz.",
            'invalid': "Yalnış dəyər daxil edilib.",
            'max_length': "Simvolların sayı maksimumu keçib.",
            'min_length': "Simvolların sayı minimumun altındadır."
            }
        )
    password = forms.CharField(
        label='Şifrənizi daxil edin:',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrə', 
        'style': 'width: 50%; min-width: 280px;'}),
        error_messages={
            'empty_value': "Boş dəyər daxil edilib.",
            'required': "Bu xana boş ola bilməz.",
            'max_length': "Simvolların sayı maksimumu keçib.",
            'min_length': "Simvolların sayı minimumun altındadır."
            }
        )
    remember_me = forms.BooleanField(required=False, label='Məni xatırla')

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.errors:
                visible.field.widget.attrs['class'] = 'form-control is-invalid'
            else:
                visible.field.widget.attrs['class'] = 'form-control'