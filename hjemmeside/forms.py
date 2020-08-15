from django import forms
import datetime

class BestillingForm(forms.Form):
    OPTIONS = (
        ('Grunnleggende','Grunnleggende'),
        ('Løftende','Løftende'),
        ('Usikker','Ønsker tips på type behandling'),
    )

    behandling = forms.ChoiceField(choices=OPTIONS)
    ønsket_dato = forms.DateField(initial=datetime.date.today)
    melding = forms.CharField(widget=forms.Textarea)
    fult_navn = forms.CharField(max_length=100)
    epost = forms.EmailField()

class KontaktForm(forms.Form):
    emne = forms.CharField(max_length=50)
    melding = forms.CharField(widget=forms.Textarea)
    epost = forms.EmailField()
