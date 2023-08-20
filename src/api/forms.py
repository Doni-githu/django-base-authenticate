from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy
User = get_user_model()


class UserCreationForm2(UserCreationForm):
    email = forms.EmailField(
        label=gettext_lazy("Email"),
        max_length=250,
        widget=forms.EmailInput(attrs={'authocomplete': 'email'})
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')