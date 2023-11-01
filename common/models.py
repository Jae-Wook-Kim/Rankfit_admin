from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Speciffic permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.email

class User(models.Model):
    userID = models.CharField(max_length=30, primary_key=True)
    userEmail = models.EmailField(max_length=45)
    userNickname = models.CharField(max_length=8)
    userAge = models.IntegerField()
    userSex = models.IntegerField()
    userWeight = models.IntegerField()
    userWD = models.CharField(max_length=10)
    anaerobicScore = models.FloatField(default=0.0)
    aerobicScore = models.FloatField(default=0.0)
    Score = models.FloatField(default=0.0)
    AgeRank = models.IntegerField(null=True, blank=True)
    CustomRank = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table='userTBL'
        managed=False