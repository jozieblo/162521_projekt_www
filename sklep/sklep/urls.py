from django.contrib import admin
from django.urls import path, include
from aplikacja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplikacja/', include('aplikacja.urls')),
    path('uzytkownicy/', views.uzytkownicy),
    path('uzytkownik_modyfikacja/<int:pk>/', views.uzytkownik_modyfikacja),
    path('uzytkownik_stworz/', views.uzytkownik_stworz),
    path('zalogowani/', views.zalogowani),
    path('zamowienia/', views.zamowienia),
    path('produkty/', views.produkty),
]
