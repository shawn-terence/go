# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(AbstractUser):
#     ROLE_CHOICES = [
#         ('admin', 'Admin'),
#         ('client', 'Client'),
#         ('expert', 'Expert'),
#         ('retired_expert', 'Retired Expert'),
#     ]

#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)

#     # Adding unique related_name to avoid clashes
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_groups',
#         blank=True,
#         help_text='The group this user belongs to.',
#         verbose_name='groups',
#     )

#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )

#     def is_expert(self):
#         return self.role in ['expert', 'retired_expert']

#     def __str__(self):
#         return self.username
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, role, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)

        user = self.model(email=email, username=username, role=role, **extra_fields)

        if password:
            user.set_password(password)

        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45, unique=True)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('expert', 'Expert'),
        ('retired_expert', 'Retired Expert'),
    ]
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='client')  

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The group this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role'] 

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"  

    def is_expert(self):
        return self.role in ['expert', 'retired_expert']

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)  # For experts
    portfolio = models.FileField(upload_to='portfolios/', null=True, blank=True)  # For experts

    def __str__(self):
        return f'{self.user.username} Profile'


# Organization model
class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.organization_name