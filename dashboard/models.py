from django.db import models
from accounts.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Building(models.Model):
    """
    Building model for the buildings at WSU.
    """
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField('last modified', auto_now=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    """
    Room model for rooms at WSU
    """
    building = models.ForeignKey(Building)
    user = models.ForeignKey(User)

    number = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField('last modified', auto_now=True)

    class Meta:
        unique_together = ('building', 'number',)


    def __str__(self):
        return '{} {}'.format(self.building.name, self.number)

    def get_building(self):
        return self.building_id

    def get_department(self):
        return self.department

    def get_user(self):
        return self.user_id

    def get_absolute_url(self):
        return reverse('room', kwargs={'pk': str(self.id)})


class Ticket(models.Model):
    """
    Tickets assigned to rooms
    """
    room = models.ForeignKey(Room)
    subject = models.CharField(max_length=255)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField('last modified', auto_now=True)
    complete = models.BooleanField("fixed", default=False)


    def get_close_url(self):
        return reverse('ticket-close', kwargs={'ticket_id': str(self.id)})


    def get_absolute_url(self):
        return reverse('ticket', kwargs={'pk': str(self.id)})

    def __str__(self):
        if len(self.notes) <= 50:
            return self.notes[0:(len(self.notes))]
        else:
            return self.notes[:50] + "..."

    def get_status(self):
        return self.status

    def get_room_id(self):
        return self.room
