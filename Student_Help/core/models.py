from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Post(models.Model):
    TYPE_CHOICES = (
        (0, 'Offer'),
        (1, 'Request'),
    )

    id = models.AutoField(primary_key=True)
    type = models.IntegerField(choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='post_images/')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def is_liked_by_user(self, user):
        return self.likes.filter(user=user).exists()


class Logement(Post):
    location = models.CharField(max_length=255)

class Transport(Post):
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departureTime = models.TimeField()

class Stage(Post):
    TYPE_INTERNSHIP_CHOICES = (
        (1, 'Worker'),
        (2, 'Technician'),
        (3, 'PFE'),
    )

    typeInternship = models.IntegerField(choices=TYPE_INTERNSHIP_CHOICES)
    company = models.CharField(max_length=255)
    duration = models.IntegerField()
    subject = models.CharField(max_length=255)


class Evenement(Post):  
    TYPE_EVENT_CHOICES = (
        (0, 'Cultural'),
        (1, 'Scientific'),
    )

    date = models.DateField()
    eventType = models.IntegerField(choices=TYPE_EVENT_CHOICES)
    club = models.CharField(max_length=255, blank=True)
    price = models.FloatField(blank=True)
    domain = models.CharField(max_length=255, blank=True)

class Recommandation(Post):
    text = models.TextField()

class Commentaire(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
