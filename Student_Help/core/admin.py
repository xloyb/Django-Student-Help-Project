from django.contrib import admin

# Register your models here.
# from .models import User
# admin.site.register(User)

from .models import Evenement
admin.site.register(Evenement)

from .models import Poste
admin.site.register(Poste)

from .models import Stage
admin.site.register(Stage)

from .models import Reaction
admin.site.register(Reaction)

from .models import Logement
admin.site.register(Logement)

from .models import Transport
admin.site.register(Transport)

from .models import Recommandation
admin.site.register(Recommandation)

from .models import EvenClub
admin.site.register(EvenClub)

from .models import EvenSocial
admin.site.register(EvenSocial)