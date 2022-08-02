from random import choices
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    def __str__(self):
        return f'{self.name}'
        
    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=50)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null = True,blank=True)
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    genre = models.fields.CharField(choices=Genre.choices,max_length=5)


class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    class Type(models.TextChoices):
        RECORDS = 'RC'
        CLOTHING = 'CL'
        POSTERS = 'PT'
        Miscellaneous = 'MC'
    types = models.fields.CharField(choices = Type.choices,max_length=10)
    description = models.fields.CharField(max_length=250)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(2000),MaxValueValidator(2022)]
    )
    sold = models.fields.BooleanField(default=True)
    band = models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.title}'



        
            
        
