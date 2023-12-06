from rest_framework import serializers
from .models import Uzytkownik, Zalogowany, Produkt, Zamowienie

class UzytkownikModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = ['id', 'nazwa', 'email', 'haslo', 'powtorz_haslo']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.email = validated_data.get('email', instance.email)
        instance.haslo = validated_data.get('haslo', instance.haslo)
        instance.powtorz_haslo = validated_data.get('powtorz_haslo', instance.powtorz_haslo)
        instance.save()
        return instance
class ZalogowanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zalogowany
        fields = ['id', 'nazwa', 'haslo']
        read_only_fields = ['id']
    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.haslo = validated_data.get('haslo', instance.haslo)
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