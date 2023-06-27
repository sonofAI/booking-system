from django.db import models


# Create your models here.

class Room(models.Model):
    ROOM_TYPES = (
        ('focus', 'Focus'),
        ('team', 'Team'),
        ('conference', 'Conference')
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100, choices=ROOM_TYPES)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    resident = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.room.name

