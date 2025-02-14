from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from api.models import Patient, Doctor, BrainScan

# Strona główna – teraz wyświetla modele (pacjentów, lekarzy, skany)
def index(request):
    patients = Patient.objects.all()[:5]  # Pobieramy 5 pacjentów
    doctors = Doctor.objects.all()[:5]  # Pobieramy 5 lekarzy
    scans = BrainScan.objects.all()[:5]  # Pobieramy 5 skanów

    return render(request, 'index.html', {
        'patients': patients,
        'doctors': doctors,
        'scans': scans,
    })

# Strona rejestracji użytkownika
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")  # Przekierowanie na stronę główną po rejestracji
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
