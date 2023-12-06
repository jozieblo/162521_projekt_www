from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Uzytkownik
from .serializers import UzytkownikModelSerializer
def index(request):
    return HttpResponse("Hello world!")

@api_view(['GET'])
def uzytkownicy(request):
    if request.method == 'GET':
        uzytkownicy = Uzytkownik.objects.all()
        serializer = UzytkownikModelSerializer(uzytkownicy, many=True)
        return Response(serializer.data)