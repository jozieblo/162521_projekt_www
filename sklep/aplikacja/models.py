from django.db import models
rodzaj_produktu = [
        ('komputer', 'komputer'),
        ('laptop', 'laptop'),
        ('tablet', 'tablet'),
        ('smartfon', 'martfon'),
    ]
status_zamowienia = [
        ('Nowe', 'Nowe'),
        ('W trakcie realizacji', 'W trakcie realizacji'),
        ('Zrealizowane', 'Zrealizowane'),
    ]


class Uzytkownik(models.Model):
    nazwa = models.CharField(max_length=35, unique=True)
    imie = models.CharField(max_length=35)
    nazwisko = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    haslo = models.CharField(max_length=35)
    telefon = models.IntegerField( )

    def __str__(self):
        return self.nazwa

class Produkt(models.Model):
    nazwa = models.CharField(max_length=50)
    kategoria = models.CharField(choices=rodzaj_produktu, max_length=20)
    cena = models.CharField(max_length=20)
    producent = models.CharField(max_length=50)
    kolor =  models.CharField(max_length=35)
    dostepnosc = models.IntegerField()
    opis = models.TextField()

    def __str__(self):
        return self.nazwa
class Zamowienie(models.Model):
    nazwa = models.CharField(max_length=35, default="Zamowienie")
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    produkty = models.ManyToManyField(Produkt)
    data_zamowienia = models.DateTimeField(auto_now_add=True)
    adres_dostawy = models.CharField(max_length=70)
    status = models.CharField(max_length=50, choices=status_zamowienia, default='Nowe')
    def __str__(self):
        return self.nazwa
class Koszyk(models.Model):
    nazwa = models.CharField(max_length=35, default="Koszyk")
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    produkty = models.ManyToManyField(Produkt)
    def __str__(self):
        return self.nazwa