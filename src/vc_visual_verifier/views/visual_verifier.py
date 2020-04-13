from django.conf import settings
from django.shortcuts import render


def verifier(request):    
    required_claims = settings.OIDC_CLAIMS_REQUIRED.split(",")
    claims = []
    if not request.user.is_anonymous:
        for claim in required_claims:
            if claim in request.user.oidc_user.userinfo:
                claims.append({ "name": claim, "provided": True  })
            else:
                claims.append({ "name": claim, "provided": False  })
    return render(request, "visual_verifier.html", {"settings": settings, "claims": claims})
