from django.contrib import admin
from django.urls import path
from hjemmeside.views import bestillingView,kontaktView

app_name = 'hjemmeside'

urlpatterns=[
    path('caroline/',kontaktView,name='caroline'),
    path('bestilling/',bestillingView,name='bestilling'),
]
