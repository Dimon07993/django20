from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegistrForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2' )




class UserProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone_number', 'country' )





    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].widget = forms.HiddenInput()



class EmailForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)