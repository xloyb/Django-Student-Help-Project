from django.conf import settings

def tailwind_version(request):
    return {'TAILWIND_VERSION': settings.TAILWIND_VERSION}