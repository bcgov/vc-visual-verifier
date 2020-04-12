from django.conf import settings
from django.shortcuts import render


def verifier(request):
    return render(request, "visual_verifier.html", {"settings": settings})
