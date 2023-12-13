from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Uzytkownik, Zamowienie, Produkt, Koszyk
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from .serializers import UzytkownikModelSerializer, ZamowienieModelSerializer, ProduktModelSerializer, UserDomyslnySerializer, KoszykModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from .permissions import Uprawnienia
def index(request):
    return HttpResponse("Hello world!")


#Uzytkownik
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated, Uprawnienia])
def uzytkownicy(request):
        if request.method == 'GET':
            lista = Uzytkownik.objects.all()
            serializer = UzytkownikModelSerializer(lista, many=True)
            return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def uzytkownik_tworzenie(request):
    if request.method == 'POST':
        serializer = UzytkownikModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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

#Produkt
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def produkty(request):
    if request.method == 'GET':
        lista = Produkt.objects.all()
        serializer = ProduktModelSerializer( lista, many=True)
        return Response(serializer.data)
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def produkt_tworzenie(request):
    if request.method == 'POST':
        serializer = ProduktModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def produkt_modyfikacja(request, pk):
    try:
        produkt = Produkt.objects.get(pk=pk)
    except Produkt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        produkt = Produkt.objects.get(pk=pk)
        serializer = ProduktModelSerializer(produkt)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProduktModelSerializer(produkt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produkt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Zamówienie

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def zamowienia(request):
    if request.method == 'GET':
        lista = Zamowienie.objects.all()
        serializer = ZamowienieModelSerializer( lista, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def zamowienie_tworzenie(request):
    if request.method == 'POST':
        serializer = ZamowienieModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def zamowienie_modyfikacja(request, pk):
    try:
        zamowienie = Zamowienie.objects.get(pk=pk)
    except Zamowienie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        zamowienie = Zamowienie.objects.get(pk=pk)
        serializer = ZamowienieModelSerializer(zamowienie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ZamowienieModelSerializer(zamowienie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        zamowienie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Koszyk
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def koszyki(request):
    if request.method == 'GET':
        lista = Koszyk.objects.all()
        serializer = KoszykModelSerializer( lista, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def koszyk_tworzenie(request):
    if request.method == 'POST':
        serializer = KoszykModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def koszyk_modyfikacja(request, pk):
    try:
        koszyk = Koszyk.objects.get(pk=pk)
    except Koszyk.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        koszyk = Koszyk.objects.get(pk=pk)
        serializer = KoszykModelSerializer(koszyk)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KoszykModelSerializer(koszyk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        koszyk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Specjalne
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def zamowienia_zrealizowane(request):
    if request.method == 'GET':
        lista = Zamowienie.objects.filter(status='Zrealizowane')
        serializer = ZamowienieModelSerializer( lista, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def uzytkownicy_specjalni(request):
    if request.method == 'GET':
        lista = Uzytkownik.objects.filter(nazwa__istartswith='t')
        serializer = UzytkownikModelSerializer( lista, many=True)
        return Response(serializer.data)


#User domyślny
@api_view(['POST'])
@permission_classes([AllowAny])
def rejestracja(request):
    if request.method == 'POST':
        serializer = UserDomyslnySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Użytkownik został pomyślnie zarejestrowany."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)