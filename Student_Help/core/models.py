from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


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

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.message}"

class Report(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('dismissed', 'Dismissed'),
    )

    REASON_CHOICES = (
        ('spam', 'Spam'),
        ('inappropriate', 'Inappropriate Content'),
        ('abuse', 'Abuse'),
        ('other', 'Other'),
    )

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return f"{self.reporter.username} reported {self.post.title} for {self.reason}"

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Student Help by MyDevify.com")
    registration_open = models.BooleanField(default=True)  

    def __str__(self):
        return self.site_name