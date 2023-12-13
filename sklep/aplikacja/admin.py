from django.contrib import admin

from .models import Uzytkownik, Zamowienie, Produkt, Koszyk

class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'email']

class ZamowienieAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'uzytkownik']

class ProduktAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'kategoria', 'cena']

class KoszykAdmin(admin.ModelAdmin):
    list_display = ['id', 'nazwa', 'uzytkownik']

admin.site.register(Uzytkownik, UzytkownikAdmin)
admin.site.register(Zamowienie,ZamowienieAdmin)
admin.site.register(Produkt, ProduktAdmin)
admin.site.register(Koszyk, KoszykAdmin)
