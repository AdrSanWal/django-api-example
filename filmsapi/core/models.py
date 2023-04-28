from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["pk"]
        verbose_name = "category"
        verbose_name_plural = "categories"


class Person(models.Model):
    GENDER_CHOICES = [("M", "Masculino"), ("F", "Femenino")]

    name = models.CharField(max_length=50)
    # photo = fields.ImageField(upload_to='../persons/%Y%m%d/', null=True, blank=True)
    photo = models.URLField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    principal_role = models.CharField(max_length=50)
    birth_date = models.DateField()
    age = models.PositiveBigIntegerField()
    birth_place = models.CharField(max_length=150)
    biography = models.TextField()

    def __str__(self):
        return f'{self._id} - {self.name}'

    class Meta:
        ordering = ["pk"]
        verbose_name = "person"
        verbose_name_plural = "people"


class Film(models.Model):
    title = models.CharField(max_length=150)
    original_title = models.CharField(max_length=150)
    state = models.CharField(max_length=10)
    original_language = models.CharField(max_length=10)
    budget = models.IntegerField(verbose_name='Presupuesto', null=True, blank=True)
    income = models.IntegerField(verbose_name='Ingresos', null=True, blank=True)
    year = models.DateField()
    image = models.URLField()
    category = models.ManyToManyField(to=Category, related_name='rel_category')
    duration = models.CharField(max_length=10)
    score = models.CharField(max_length=5)
    description = models.TextField()
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
