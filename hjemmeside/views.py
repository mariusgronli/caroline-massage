from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail,BadHeaderError

from .forms import KontaktForm

# Create your views here.
class HomepageView(TemplateView):
    template_name = "massasje/index.html"

class GavekortView(TemplateView):
    template_name = "massasje/gavekort.html"

class BestillingView(TemplateView):
    template_name = "massasje/bestilling.html"

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
