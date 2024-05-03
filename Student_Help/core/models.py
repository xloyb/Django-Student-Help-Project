from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.comment[:20]}"

class Image(models.Model):
    # Assuming you want to store images as separate files
    image = models.ImageField(upload_to='posts/images/', blank=True)

class Post(models.Model):
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)
    TYPE_CHOICES = (
        (0, 'Offer'),
        (1, 'Request'),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, blank=True, null=True)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE, blank=True, null=True)
    logement = models.ForeignKey('Logement', on_delete=models.CASCADE, blank=True, null=True)
    transport = models.ForeignKey('Transport', on_delete=models.CASCADE, blank=True, null=True)
    comments = models.ManyToManyField(Reaction, related_name='posts', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.get_type_display()}"

class Event(models.Model):
    intitule = models.CharField(max_length=255)
    description = models.TextField()
    lieu = models.CharField(max_length=255)
    contactInfo = models.CharField(max_length=255)
    TYPE_CHOICES = (
        (1, 'Cultural'),
        (2, 'Scientific'),
    )
    type = models.IntegerField(choices=TYPE_CHOICES)
    evenClub = models.ForeignKey('EvenClub', on_delete=models.CASCADE, blank=True, null=True)
    evenSocial = models.ForeignKey('EvenSocial', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.intitule}"

class EvenClub(models.Model):
    club = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.club} - {self.specialite}"

class EvenSocial(models.Model):
    prix = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Prix: {self.prix}"

class Stage(models.Model):
    TYPE_CHOICES = (
        (1, 'Worker'),
        (2, 'Technician'),
        (3, 'PFE'),
    )
    typeStg = models.IntegerField(choices=TYPE_CHOICES)
    societe = models.CharField(max_length=255)
    duree = models.IntegerField()
    sujet = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.societe} - {self.get_type_display()}"

class Logement(models.Model):
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    contactInfo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.localisation} - {self.description[:20]}"



class Transport(models.Model):
    # Add fields specific to transport offers/requests
    # Here are some examples:
    departure_location = models.CharField(max_length=255)
    arrival_location = models.CharField(max_length=255)
    departure_date = models.DateField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    # You can add additional fields like capacity, vehicle type, etc.

    def __str__(self):
        return f"Transport: {self.departure_location} - {self.arrival_location}"
