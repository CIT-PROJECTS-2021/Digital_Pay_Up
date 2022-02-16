from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
import random

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, phone_number, password=None):
        if not email:
            raise ValueError('Users must have a valid email address!')
        account = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone_number=phone_number
        )
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, first_name, last_name, email, username, phone_number, password):
        user = self.create_user(first_name, last_name, email, username, phone_number, password)
        user.is_admin = True
        user.is_staff = True
        user.save()

        return user

class Profile(AbstractBaseUser, PermissionsMixin):
    account_id = models.CharField(max_length=7, validators=[MinLengthValidator(7), MaxLengthValidator])
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    username = models.CharField(max_length=60, unique=True)
    phone_number = models.CharField(max_length=17, unique=True)

    verification_code = models.CharField(default=f"{random.randint(111111, 999999)}", max_length=9)
    tax_id = models.CharField(max_length=60)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

