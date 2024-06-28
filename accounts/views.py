from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import Users
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm  # Assurez-vous d'avoir votre propre formulaire d'inscription

def connexion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            Nom = form.cleaned_data['nom']
            password = form.cleaned_data['password']

            # Authentifier l'utilisateur
            user = authenticate(request, username=Nom, password=password)
            user.first_name =   Nom
            if user is not None:
                login(request, user)
                # Rediriger vers la page d'accueil ou une autre page après la connexion
                return redirect('index')
            else:
                # Gérer le cas où l'authentification a échoué
                return render(request, "account/login.html", {'form': form, 'error': 'E-mail ou mot de passe incorrect.'})
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            nom = form.cleaned_data['nom']
            password = form.cleaned_data['password']
            type = form.cleaned_data['type']
            motif = form.cleaned_data['motif']

            existing_users = User.objects.filter(username=nom)
            if existing_users.exists():
                # Gérer le cas où l'utilisateur existe déjà
                return render(request, "accounts/signup.html", {'form': form, 'error': 'Un compte avec cet e-mail existe déjà.'})
            else:
                # Créer un nouvel utilisateur
                user = User.objects.create_user(username=nom, password=password)
                # Enregistrement des autres champs personnalisés

                user.save()
            # Rediriger vers la page d'accueil ou une autre page après l'inscription
            return redirect('index')
    else:
        # Afficher le formulaire d'inscription vide
        form = SignupForm()

    return render(request, "accounts/signup.html", {'form': form})