
from .forms import EmailForm
from django.contrib import messages
from django.conf import settings




import random
import string
import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, FormView
from django.core.mail import send_mail

from users.forms import UserRegistrForm, UserProfileForm
from users.models import User
from config.settings import EMAIL_HOST_USER

class RegisterView(CreateView):
    model = User
    form_class = UserRegistrForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()

        url = f"http://{host}/users/email-confirm/{token}/"

        send_mail(
            subject="Подтверждение регистрации",
            message=f"Подтвердите свой аккаунт перейдя по ссылке: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordResetView(FormView):
    template_name = 'users/password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            form.add_error(None, 'Пользователь с таким адресом электронной почты не найден.')
            return self.form_invalid(form)

        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        user.password = make_password(new_password)
        user.save()

        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        #subject = 'Восстановление пароля'
        #message = f'Ваш новый пароль: {new_password}'
        #from_email = EMAIL_HOST_USER
        #send_mail(subject, message, from_email, [email])

        return super().form_valid(form)


