from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'Actor'

    def __str__(self):
        return f'{self.name} : {self.birthdate}'


class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    imdb = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    genre = models.CharField(max_length=200)
    actor = models.ManyToManyField(Actor)

    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return f'{self.name} : {self.year}'


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_date = models.DateField()
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'Comment'

    def __str__(self):
        return f'{self.movie_id} -- {self.user_id} -- {self.created_date}'
