from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
           nom = form.cleaned_data['nom']
           prenom = form.cleaned_data['prenom']
           email = form.cleaned_data['email']
           sujet = form.cleaned_data['sujet']
           content = form.cleaned_data['content']
           
           html = render_to_string('send.html', {
               'nom' : nom,
               'prenom' : prenom,
               'email' : email,
               'sujet' : sujet,
               'content': content
           })

           send_mail('The contact form subject', 'This is the message', 'name@gmail.com', ['joeldragnir490@gmail.com'], html_message=html)
        return redirect('index')
    else:
        form = Contact
    return render(request, 'contact.html', {'form': form})