from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail,BadHeaderError

from .forms import BestillingForm,KontaktForm

# Create your views here.
class HomepageView(TemplateView):
    template_name = "massasje/index.html"

def kontaktView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = KontaktForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            emne = form.cleaned_data['emne']
            epost = form.cleaned_data['epost']
            melding_raw = form.cleaned_data['melding']
            #formater melding som blir sendt i mail
            melding = '{} \n avsender: {}'.format(melding_raw,epost)
            try:
                send_mail(emne, melding, epost, ['mariusgronli@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Noe gikk galt, send mail til: mariusgronli@gmail.com')
            return render(request,'massasje/info.html',{'form':form,'kunde':epost})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = KontaktForm()
    return render(request, 'massasje/info.html', {'form': form})


def bestillingView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BestillingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            behandling = form.cleaned_data['behandling']
            ønsket_dato = form.cleaned_data['ønsket_dato']
            melding_raw = form.cleaned_data['melding']
            fult_navn = form.cleaned_data['fult_navn']
            epost = form.cleaned_data['epost']
            #formater melding som blir sendt i mail
            emne = 'Bestilling fra {}'.format(fult_navn)
            melding = 'Melding fra kunde: {}\n Ønsket behandling:{}\n Ønsket dato: {}\n Sendt fra: {}'.format(melding_raw,behandling,ønsket_dato,epost)
            try:
                send_mail(emne, melding, epost, ['mariusgronli@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Noe gikk galt, send mail til: mariusgronli@gmail.com')
            return render(request,'massasje/bestilling.html',{'form':form,'kunde':fult_navn})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BestillingForm()
    return render(request, 'massasje/bestilling.html', {'form': form})
