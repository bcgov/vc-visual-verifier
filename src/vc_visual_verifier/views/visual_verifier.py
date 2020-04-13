from django.conf import settings
from django.shortcuts import render


def verifier(request):
    required_claims = settings.OIDC_CLAIMS_REQUIRED.split(",")
    claims = []
    for claim in required_claims:
        if request.user.oidc_user.userinfo[claim] is not None:
            claims.append({ "name": claim, "provided": True  })
        else:
            claims.append({ "name": claim, "provided": True  })
    return render(request, "visual_verifier.html", {"settings": settings, "claims": claims})
