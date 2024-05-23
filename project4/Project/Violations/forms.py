from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Application
from .validators import validate_cyrillic, validate_telephone


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

class signUpForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        min_length=6,  # Устанавливаем минимальную длину логина в 6 символов
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
        help_text="Обязательно. Минимум 6 символов."  # Добавляем подсказку для пользователя
    )
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль', 'required': 'required'}),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль', 'required': 'required'}),
    )

    last_name = forms.CharField(
        label="Фамилия",
        validators=[validate_cyrillic],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию', 'required': 'required'})
    )
    first_name = forms.CharField(
        label="Имя",
        validators=[validate_cyrillic],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя', 'required': 'required'})
    )
    patronymic = forms.CharField(
        label="Отчество",
        validators=[validate_cyrillic],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отчество', 'required': 'required'})
    )

    telephone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите телефон', 'required': 'required', 'placeholder': '+7(XXX)-XXX-XX-XX'}),
        validators=[validate_telephone]  # Добавляем валидатор для телефона
    )

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'telephone', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email', 'required': 'required'}),

        }




class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['car_number', 'description', 'image']
        widgets = {
            'car_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер автомобиля', 'required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-2', 'required': 'required'})
        }