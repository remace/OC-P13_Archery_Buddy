""" accounts models """
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """User and superuser factory class"""

    def create_user(self, pseudo, password=None, **extra_fields):
        """create user"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)
        # authentification keys verification
        if not pseudo:
            raise ValueError("Users must have Pseudo")
        if not password:
            raise ValueError("User must have Password")

        user_obj = self.model(pseudo=pseudo, **extra_fields)

        user_obj.set_password(password)
        user_obj.is_active = True
        user_obj.is_staff = extra_fields["is_staff"]
        user_obj.is_admin = extra_fields["is_admin"]
        user_obj.is_superuser = extra_fields["is_superuser"]
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, pseudo, password=None, **extra_fields):
        """create super user"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(pseudo, password=password, **extra_fields)


class User(AbstractBaseUser):
    """User Model.
    credentials are pseudo (unique) and password
    """

    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pseudo = models.CharField(unique=True, max_length=32, blank=True, null=True)

    # registration create and update fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # flag to delete user without deleting it form database
    is_active = models.BooleanField(default=True)

    # permissions
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    # use email for authentification
    USERNAME_FIELD = "pseudo"

    def __str__(self):
        return f"{self.pseudo}"

    def get_full_name(self) -> str:
        """gets a str with full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.pseudo}"

    def has_perm(self, perm, obj=None):
        """returns whether the User has permission or not"""
        return True

    def has_module_perms(self, app_label):
        """returns whether the User has module permission or not"""
        return True

    class Meta:
        verbose_name: "user"
        verbose_name_plural: "users"
