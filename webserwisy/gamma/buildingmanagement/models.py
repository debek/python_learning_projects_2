from django.db import models
#Jak cos sie wywali todczas procesu to przywraca do bazy jakby nic sie nie stalo .transactions
from django.db import transaction
from django.db.models import F

class Room(models.Model):
    name = models.CharField(max_length=100)
    people_count = models.PositiveSmallIntegerField(default=0) #zajmuje mniej miejsca w pamieci i nie moze byc na minusie

    def __str__(self):
        return self.name

    @transaction.atomic
    def move_people_t(self, other_room, count=1):

        #Msowo mozemy podmienic rzeczy w QuerySet
        Room.objects.filter(pk=self.pk).update(people_count=F("people_count") - count)

        self.people_count -= count
        self.save()
        other_room.people_count += count
        other_room.save()

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.room.name}/{self.date}"
