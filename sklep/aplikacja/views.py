from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Uzytkownik, Zalogowany, Zamowienie, Produkt
from .serializers import UzytkownikModelSerializer, ZalogowanyModelSerializer, ZamowienieModelSerializer, ProduktModelSerializer
def index(request):
    return HttpResponse("Hello world!")

@api_view(['GET']) #Lista wszystkich uzytkownikow
def uzytkownicy(request):
    if request.method == 'GET':
        lista = Uzytkownik.objects.all()
        serializer = UzytkownikModelSerializer(lista, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def uzytkownik_modyfikacja(request, pk):
    try:
        uzytkownik = Uzytkownik.objects.get(pk=pk)
    except Uzytkownik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        uzytkownik = Uzytkownik.objects.get(pk=pk)
        serializer = UzytkownikModelSerializer(uzytkownik)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UzytkownikModelSerializer(uzytkownik, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uzytkownik.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['POST'])
def uzytkownik_stworz(request):
    if request.method == 'POST':
        serializer = UzytkownikModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def zalogowani(request):
    if request.method == 'GET':
        lista = Zalogowany.objects.all()
        serializer = ZalogowanyModelSerializer( lista, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def zamowienia(request):
    if request.method == 'GET':
        lista = Zamowienie.objects.all()
        serializer = ZamowienieModelSerializer( lista, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def produkty(request):
    if request.method == 'GET':
        lista = Produkt.objects.all()
        serializer = ProduktModelSerializer( lista, many=True)
        return Response(serializer.data)