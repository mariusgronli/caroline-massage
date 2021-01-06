from django import forms
import datetime

class KontaktForm(forms.Form):
    emne = forms.CharField(max_length=50)
    melding = forms.CharField(widget=forms.Textarea)
    epost = forms.EmailField()
