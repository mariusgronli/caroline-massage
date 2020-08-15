from django.db import models

# Create your models here.
# class KontaktModel(models.Model):
#     #behandling valgmuligheter
#     GRUNNLEGGENDE = 'Grunnleggende'
#     LØFTENDE = 'Løftende'
#     USIKKER = 'Usikker'
#     ANNET = 'Annet'
#     BEHANDLING_CHOICES = [(GRUNNLEGGENDE,'Grunnleggende'),(LØFTENDE,'Løftende'),
#         (USIKKER,'Usikker'),(ANNET,'Annet')]
#
#     fornavn = models.CharField(max_length=100)
#     etternavn = models.CharField(max_length=100)
#     telefonnummer = etternavn = models.CharField(max_length=8)
#     epost = models.EmailField(max_length=100)
#     behandling = models.CharField(max_length=10,choices=BEHANDLING_CHOICES,default=GRUNNLEGGENDE)
#     forespørsel = models.CharField(max_length=500,blank=True,null=True)
#
#     def __str__(self):
#         return self.etternavn
#
#     def get_absolute_url(self):
#         return reverse('home')
