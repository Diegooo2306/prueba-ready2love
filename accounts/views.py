from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == "POST":
        display_name = request.POST.get("username", "").strip() or "Matcher"
        request.session["display_name"] = display_name

        remember_me = request.POST.get("remember_me") == "on"
        if remember_me:
            request.session.set_expiry(60 * 60 * 24 * 14)
        else:
            request.session.set_expiry(0)

        User = get_user_model()
        demo_user, created = User.objects.get_or_create(username="demo_matcher")
        if created:
            demo_user.set_unusable_password()
            demo_user.save()

        login(request, demo_user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("dashboard")

    return render(request, "accounts/login.html")


@login_required
def dashboard(request):
    status_options = [
        "Asignar cita",
        "Cita asignada",
        "En espera",
        "Sin asignar",
        "Cancelación de plan",
        "Dado de baja",
        "Término de membresía",
    ]
    lover = {
        "name": "Persona",
        "remaining_dates": 7,
        "status": "Asignar cita",
        "date_with": "Persona",
    }
    context = {
        "status_options": status_options,
        "lover": lover,
    }
    return render(request, "accounts/dashboard.html", context)
