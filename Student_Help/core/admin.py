from django.contrib import admin
from .models import Post,Logement, Transport, Stage, Evenement, Recommandation, Commentaire, Like,Notification, Report, SiteSettings

# Register only the concrete post models with the admin site
admin.site.register(Post)
admin.site.register(Logement)
admin.site.register(Transport)
admin.site.register(Stage)
admin.site.register(Evenement)
admin.site.register(Recommandation)
admin.site.register(Commentaire)
admin.site.register(Like)
admin.site.register(Notification)
admin.site.register(Report)
admin.site.register(SiteSettings)



