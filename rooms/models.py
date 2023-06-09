from django.db import models

# Create your models here.

class Room(models.Model):
    ROOM_TYPES = (
        ('focus', 'Focus'),
        ('team', 'Team'),
        ('conference', 'Conference')
    )

    name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=100)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name
