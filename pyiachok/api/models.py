import os
from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

User = get_user_model()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    photo = models.ImageField(upload_to=os.path.join('user_auth', 'img'), default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    sex = models.CharField(max_length=30)

    def __str__(self):
        return self.user


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "http://localhost:3000{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
