from django.contrib import admin
from .models import uygulama
# from Uygulama.models import uygulama
# Register your models here.

class uygulamaAdmin(admin.ModelAdmin):
    list_display= ['name_surname','id_nummer']
    search_fields = ['name_surname']
    class Meta:
        model=uygulama

admin.site.register(uygulama,uygulamaAdmin)


