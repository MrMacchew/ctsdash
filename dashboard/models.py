from django.db import models
from accounts.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

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

    def get_absolute_url(self):
        return reverse('building-rooms', kwargs={'pk': str(self.id)})


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
    working = models.BooleanField('status', default=True)

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
        return reverse('actions:ticket-close', kwargs={'ticket_id': str(self.id)})

    def get_open_url(self):
        return reverse('actions:ticket-open', kwargs={'ticket_id': str(self.id)})

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



@receiver(post_save, sender=Ticket)
def update_room_status(*args, **kwargs):
    print("Post Save Ran")
    room = Room.objects.get(id=kwargs['instance'].room.id)
    if (kwargs['instance'].complete):
        openTickets = Ticket.objects.filter(room=kwargs['instance'].room, complete=False)
        print(openTickets.count())
        if (openTickets.count() <= 0):
            room.working = True
        else:
            room.working = False
    else:
        room.working = False

    room.save()


@receiver(post_delete, sender=Ticket)
def update_room_status_on_delete(sender, **kwargs):
    print("Post Delete Ran")

    room = Room.objects.get(id=kwargs['instance'].room.id)
    openTickets = Ticket.objects.filter(room=kwargs['instance'].room, complete=False)
    if (openTickets.count() <= 0):
        room.working = True
    else:
        room.working = False
    room.save()

