from django.db import models
from accounts.models import Profile
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Wallet(models.Model):
    account = models.ForeignKey(profile)


def generate_wallet_id():
    pass

def generate_transaction_id():
    pass


