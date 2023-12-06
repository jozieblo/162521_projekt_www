from django.contrib import admin

from .models import Uzytkownik, Zalogowany, Zamowienie, Produkt

class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'haslo']

class ZalogowanyAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'haslo']

class ZamowienieAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'uzytkownik']

class ProduktAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'kategoria', 'cena']

admin.site.register(Uzytkownik, UzytkownikAdmin)
admin.site.register(Zalogowany, ZalogowanyAdmin)
admin.site.register(Zamowienie,ZamowienieAdmin)
admin.site.register(Produkt, ProduktAdmin)
