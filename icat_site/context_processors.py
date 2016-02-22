from django.contrib.sites.models import Site
from django.conf import settings

def site(request):
    return { 'site': Site.objects.get_current() }

def conference_site(request):
    return { 'CONFERENCE_SITE': settings.CONFERENCE_SITE }
