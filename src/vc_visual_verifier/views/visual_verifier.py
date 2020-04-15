from django.conf import settings
from django.shortcuts import redirect, render, reverse


def verifier(request):
    required_claims = settings.OIDC_CLAIMS_REQUIRED.split(",")
    claims = []
    if not request.user.is_anonymous:
        for claim in required_claims:
            if claim in request.user.oidc_user.userinfo:
                claims.append(
                    {
                        "name": claim,
                        "value": request.user.oidc_user.userinfo[claim],
                        "provided": True,
                    }
                )
            else:
                claims.append({"name": claim, "provided": False})
    return render(
        request, "visual_verifier.html", {"settings": settings, "claims": claims}
    )


def authorize(request):
    return redirect(
        reverse("oidc_auth_request")
        + f"?pres_req_conf_id={settings.VC_AUTHN_PRES_REQ_CONF_ID}"
    )
