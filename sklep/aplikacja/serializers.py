from rest_framework import serializers
from .models import Uzytkownik, Produkt, Zamowienie, Koszyk
from django.contrib.auth.models import User
class UzytkownikModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = ['id', 'nazwa', 'imie', 'nazwisko', 'email', 'haslo', 'telefon']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.email = validated_data.get('email', instance.email)
        instance.haslo = validated_data.get('haslo', instance.haslo)
        instance.telefon= validated_data.get('telefon', instance.telefon)
        instance.save()
        return instance


class ZamowienieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields = ['id', 'nazwa', 'uzytkownik', 'produkty', 'data_zamowienia', 'adres_dostawy', 'status']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.uzytkownik = validated_data.get('uzytkownik', instance.uzytkownik)
        instance.produkty = validated_data.get('produkty', instance.produkty)
        instance.data_zamowienia = validated_data.get('data_zamowienia', instance.data_zamowienia)
        instance.adres_dostawy = validated_data.get('adres_dostawy', instance.adres_dostawy)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

class ProduktModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = ['id', 'nazwa', 'kategoria', 'cena', 'producent', 'kolor', 'dostepnosc', 'opis']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kategoria = validated_data.get('kategoria', instance.kategoria)
        instance.cena = validated_data.get('cena', instance.cena)
        instance.producent = validated_data.get('producent', instance.producent)
        instance.kolor = validated_data.get('kolor', instance.kolor)
        instance.dostepnosc = validated_data.get('dostepnosc', instance.dostepnosc)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance
class KoszykModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Koszyk
        fields = ['id', 'nazwa', 'uzytkownik', 'produkty']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.uzytkownik = validated_data.get('uzytkownik', instance.uzytkownik)
        instance.produkty = validated_data.get('produkty', instance.produkty)
        instance.save()
        return instance

class UserDomyslnySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

