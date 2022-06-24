""" Accounts models """
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """ User and superuser factory class
    """
    def create_user(self, pseudo, password=None, is_active=True, is_staff=False, is_admin=False):
        """ create user """
        # authentification keys verification
        if not pseudo:
            raise ValueError('Users must have email Address')
        if not password:
            raise ValueError('User must have Password')

        user_obj = self.model(
            pseudo=pseudo,
        )

        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.save(using=self._db)
        return user_obj


    def create_superuser(self, email, password=None):
        """ create super user """
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    """User Model.
    credentials are pseudo (unique) and password
    """
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    email= models.EmailField()
    pseudo = models.CharField(unique=True, max_length=32, blank=True, null=True)

    # registration create and update fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # flag to delete user without deleting it form database
    is_active = models.BooleanField(default=True)

    # permissions
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    #use email for authentification
    USERNAME_FIELD = 'pseudo'


    def __str__(self):
        return f"{self.email}"


    def get_full_name(self) -> str:
        """ gets a str with full name """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.pseudo}"


    def has_perm(self, perm, obj=None):
        """ returns whether the User has permission or not """
        return True


    def has_module_perms(self, app_label):
        """ returns whether the User has module permission or not """
        return True
