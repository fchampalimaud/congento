from django.http import JsonResponse

from .models import InstitutionalEmailDomain


def validate_institution(request):
    email = request.GET.get("email", None)

    institution_recognized = False

    if email and "@" in email:
        domain = email.split("@")[1]

        institution_recognized = InstitutionalEmailDomain.objects.filter(
            domain=domain
        ).exists()

    data = {"institution_recognized": institution_recognized}
    return JsonResponse(data)
