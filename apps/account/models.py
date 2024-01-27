from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class AccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise TypeError('Invalid phone number')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        if not password:
            raise TypeError('password did not come!')
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


GENDER_CHOICES = (
    (0, "Male"),
    (1, "Female")
)


class City(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.name}"


class BaseUser(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    name = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=225, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities', blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
