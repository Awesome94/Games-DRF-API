from django.db import models
from datetime import datetime
from django.utils import timezone

# # Create your models here.
# class Game(models.Model):
#     created = models.DateTimeField(auto_now=True)
#     name = models.CharField(max_length=200, blank='True', default='')
#     release_date = models.DateTimeField(default = timezone.make_aware(datetime.now(), timezone.get_current_timezone()))
#     game_category = models.CharField(max_length=200, blank=True, default='')
#     played =models.BooleanField(default=False)

#     class meta:
#         odering = ('name',)
'''
The Game class is a subclass of the django.db.models.Model class. 
Each defined attribute represents a database column or field.
'''
#adding postgres sql.

class  GameCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering  = ('name',)

    def __str__(self):
        return self.name

class Game(models.Model):
    owner = models.ForeignKey(
        'auth.User', 
        related_name = 'games',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True)
    game_category = models.ForeignKey(
        GameCategory, 
        related_name = 'games',
        on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    played = models.BooleanField(default=False)

    class meta:
        ordering = ('name,')
    
    def __str__(self):
        return self.name

class Player (models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, default='', unique=True)
    gender = models.CharField(
        max_length=2,
        choices = GENDER_CHOICES,
        default = MALE,
        )
    class Meta:
        ordering = ('name',)
        
        def __str__(self):
            return self.name

class PlayerScore(models.Model):
    player = models.ForeignKey(
        Player,
        related_name = 'scores',
        on_delete = models.CASCADE)
    game = models.ForeignKey(
        Game,
        on_delete = models.CASCADE)
    score = models.IntegerField()
    score_date = models.DateTimeField()

    class Meta:
        # Order by descending
        ordering = ('-score',)




