from django.db import models

# Create your models here.


class uygulama(models.Model):
    name_surname=models.CharField(max_length=120,verbose_name='İsim-Soyisim')
    birt_date=models.DateField(verbose_name='Doğum Tarihi')
    id_nummer=models.CharField(max_length=11,verbose_name='TC Numarası')
    gender=models.CharField(max_length=120,verbose_name='Cinsiyet')
    school=models.TextField(verbose_name='Okul')



