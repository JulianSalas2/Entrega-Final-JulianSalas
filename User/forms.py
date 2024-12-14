from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}
        
#          ----------------------------------------Form de editar Usuario--------------------------------------------             \
    
class UserEditForm(UserChangeForm):

        # Obligatorios
        password = None
        email = forms.EmailField(label="Ingrese su email:")
        last_name = forms.CharField(label="Apellido")
        first_name = forms.CharField(label="Nombre")
        imagen = forms.ImageField(label="Avatar",required=False)
        
        
        # No obligatorios
        # last_name = forms.CharField()
        # first_name = forms.CharField()

        class Meta:
            model = User
            fields = [
                'email',
                'last_name',
                'first_name',
                'imagen'
                # 'last_name',
                # 'first_name'
            ]
            help_texts = {k:"" for k in fields}

#           ---------------------------------------formulario de Carga de Avatar------------------------------------------------------

