import secrets
import string
import random

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User

CHARS = '+-*!&$#?=abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f"Для подтверждения почты перейдите по ссылке: {url} ",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class ResetPassword(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/reset_password.html')

    def post(self, request):
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        new_password = ''
        for i in range(10):
            new_password += random.choice(CHARS)

        message = (f'Ваш новый пароль: {new_password}'
                   f'  Сохраняйте в тайне!')
        send_mail(
            subject='Новый пароль',
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect('users:login')
