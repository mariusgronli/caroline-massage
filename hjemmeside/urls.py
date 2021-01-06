from django.contrib import admin
from django.urls import path
from hjemmeside.views import BestillingView,kontaktView,GavekortView

app_name = 'hjemmeside'

urlpatterns=[
    path('caroline/',kontaktView,name='caroline'),
    path('bestilling/',BestillingView.as_view(),name='bestilling'),
    path('gavekort/',GavekortView.as_view(),name='gavekort')
]
