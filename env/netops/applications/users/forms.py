from django import forms
from .models import User
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):

    password_1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresar contraseña'
            }
        )
    )

    password_2 = forms.CharField(
        label='Repetir contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña'
            }
        )
    )

    # Validar que las contraseñas 1 y 2 son iguales
    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')

        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password_2
    
    # Definir los campos del modelo a mostrar
    class Meta:
        model = User
        fields = (
            'email',
            'nombre',
            'apellido',
        )

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder':"Ingresar email"
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresar contraseña'
            }
        )
    )

    # Validaciones para el formulario de Login
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Usuario o contraseña incorrecto')
        else:
            raise forms.ValidationError('Por favor, ingresa un email y una contraseña')
        return cleaned_data

class UpdatePasswordForm(forms.Form):
    password_1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresar contraseña'
            }
        )
    )

    password_2 = forms.CharField(
        label='Repetir contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña'
            }
        )
    )

    