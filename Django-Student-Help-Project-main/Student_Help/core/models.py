from django.db import models
from datetime import date

#USER
class User (models.Model):
    nom = models.CharField(max_length = 100)
    prenom = models.CharField(max_length = 100)
    email= models.EmailField()
    telephone = models.CharField(max_length = 8)
    def __str__(self) :
        return self.nom+""+self.prenom+""+self.email+""+self.telephone
#EVENEMENT
class Evenement (models.Model):
    intitule=models.CharField()
    description = models.TextField(default='Non definie')
    lieu=models.CharField()
    contactinfo=models.CharField()
    def __str__(self) :
        return self.intitule+""+self.description+""+self.lieu+""+self.contactinfo
#POSTE
class Poste(models.Model):
    OFFRE = 0
    DEMANDE = 1

    TYPE_CHOICES = [
        (OFFRE, 'Offre'),
        (DEMANDE, 'Demande'),
    ]

    image = models.ImageField(blank=True)
    type = models.IntegerField(choices=TYPE_CHOICES)
    date = models.DateField()

    def __str__(self):
        return self.type+""+self.date

class Stage(models.Model):
    OUVRIER = 1
    TECHNICIEN = 2
    PFE = 3

    TYPE_CHOICES = [
        (OUVRIER, 'Ouvrier'),
        (TECHNICIEN, 'Technicien'),
        (PFE, 'PFE'),
    ]

    typeStg = models.IntegerField(choices=TYPE_CHOICES)
    societe = models.CharField(max_length=100)
    duree = models.IntegerField()
    sujet = models.CharField(max_length=200)
    contactinfo = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=True)
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return self.typeStg+""+self.societe+""+self.duree+""+self.sujet+""+self.contactinfo+""+self.specialite
# Réaction 
class Reaction(models.Model):
    commentaire = models.CharField(max_length=255)
    like = models.BooleanField(default=False)
    def __str__(self) :
        return self.commentaire+""+self.like
# Logement
class Logement(models.Model):
    description = models.CharField(max_length=255)
    localisation =models.CharField(max_length=255)
    contactinfo = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.description+""+self.localisation+""+self.contactinfo

# Transport
class Transport(models.Model):
    depart = models.CharField(max_length=255)
    destination =models.CharField(max_length=255)
    heuredep=models.TimeField()
    nbrsieges=models.IntegerField()
    contactinfo = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.depart+""+self.destination+""+self.heuredep+""+self.nbrsieges+""+self.contactinfo

#Recommandation
class Recommandation (models.Model):
    texte=models.CharField(max_length=255)
    def __str__(self):
        return self.texte
#EvenClub
class EvenClub(models.Model):
    club=models.CharField(max_length=255)
    def __str__(self):
        return self.club
#EvenSocial
class EvenSocial(models.Model):
    prix=models.DecimalField(max_digits=10 , decimal_places=3)
    def __str__(self):
        return self.prix
