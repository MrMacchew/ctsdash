from django.db import models
from accounts.models import User

# Create your models here.
class Building(models.Model):
    """
    Building model for the buildings at WSU.
    """
    building_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    @property
    def __str__(self):
        return self.building_name

class Room(models.Model):
    """
    Room model for rooms at WSU
    """
    building_id = models.ForeignKey(Building)
    room_number = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    user_id = models.ForeignKey(User)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    @property
    def __str__(self):
        return self.room_number

    def get_building(self):
        return self.building_id

    def get_department(self):
        return self.department

    def get_user(self):
        return self.user_id

class Ticket(models.Model):
    """
    Tickets assigned to rooms
    """
    room_id = models.ForeignKey(Room)
    status = models.CharField(max_length=255)
    notes = models.TextField()
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    @property
    def __str__(self):
        if len(self.notes) <= 50:
            return self.notes[0:(len(self.notes))]
        else:
            return self.notes[:50] + "..."

    def get_status(self):
        return self.status

    def get_room_id(self):
        return self.room_id