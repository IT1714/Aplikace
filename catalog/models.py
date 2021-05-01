import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Game(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular game across whole library')
    game_img = models.ImageField(upload_to='img/%Y/%m' ,blank=True,null=True)
    slideshow_img_1 = models.ImageField(upload_to='img/%Y/%m', blank=True, null=True)
    slideshow_img_2 = models.ImageField(upload_to='img/%Y/%m', blank=True, null=True)
    slideshow_img_3 = models.ImageField(upload_to='img/%Y/%m', blank=True, null=True)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the game')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this game')

    score = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(10)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('game-detail', args=[str(self.id)])


class Developer(models.Model):
    """Model representing an author."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular game across whole library')
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img/%Y/%m', blank=True, null=True)
    headquarters = models.CharField(max_length=100)
    founded = models.DateField(null=True, blank=True)
    employees=  models.IntegerField(validators=[MinValueValidator(0)])


    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('developer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}, {self.headquarters}'