from django.db import models


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
