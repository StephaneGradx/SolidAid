from django import forms


class Contact(forms.Form):
    nom = forms.CharField(max_length=128)
    prenom = forms.CharField(max_length=128)
    email = forms.EmailField()
    sujet = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)