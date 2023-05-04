from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager. The email is the field
    for authentication instead of username.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("El email es obligatorio"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create a SuperUser with email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        true_fields = ["is_staff", "is_superuser"]
        for field in true_fields:
            if extra_fields.get(field) is not True:
                raise ValueError(_(f"Un superusuario debe tener {field}=True."))
        return self.create_user(email, password, **extra_fields)

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]
        verbose_name = "category"
        verbose_name_plural = "categories"


class Person(models.Model):
    GENDER_CHOICES = [("M", "Masculino"), ("F", "Femenino"), ("N", "No definido")]

    name = models.CharField(max_length=50)
    photo = models.URLField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    principal_role = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    birth_place = models.CharField(max_length=150, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.pk} - {self.name}'

    class Meta:
        ordering = ["pk"]
        verbose_name = "person"
        verbose_name_plural = "people"


class Film(models.Model):
    title = models.CharField(max_length=150)
    original_title = models.CharField(max_length=150)
    state = models.CharField(max_length=20)
    original_language = models.CharField(max_length=50)
    budget = models.CharField(max_length=20,
                              verbose_name='Presupuesto',
                              null=True, blank=True)
    income = models.CharField(max_length=20,
                              verbose_name='Ingresos',
                              null=True, blank=True)
    year = models.DateField()
    image = models.URLField()
    certification = models.CharField(max_length=10, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(to=Category,
                                      related_name='rel_category')
    duration = models.CharField(max_length=10, null=True, blank=True)
    score = models.CharField(max_length=5)
    director = models.ManyToManyField(to=Person, related_name='rel_director')
    characters = models.ManyToManyField(to=Person, related_name='rel_characters')
    screenplay = models.ManyToManyField(to=Person, related_name='rel_screenplay')
    story = models.ManyToManyField(to=Person, related_name='rel_story')
    novel = models.ManyToManyField(to=Person, related_name='rel_novel')
    writer = models.ManyToManyField(to=Person, related_name='rel_writer')
    cast = models.ManyToManyField(to=Person, related_name='rel_cast')

    @property
    def only_year(self):
        return self.year.strftime('%Y')

    class Meta:
        ordering = ["pk"]
        verbose_name = "film"
        verbose_name_plural = "films"
