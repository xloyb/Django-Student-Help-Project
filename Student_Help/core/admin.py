from django.contrib import admin
from .models import Poste, Reaction, Evenement, Stage, Logement, Transport, EvenSocial, EvenClub, recomondation
# from .models import Poste, Reaction,Evenement,Stage

admin.site.register(Poste)
admin.site.register(Reaction)
admin.site.register(Evenement)
admin.site.register(Stage)
admin.site.register(Logement)
admin.site.register(Transport)
admin.site.register(EvenSocial)
admin.site.register(EvenClub)
admin.site.register(recomondation)
