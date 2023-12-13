from django.contrib import admin
from django.urls import path, include
from aplikacja import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplikacja/', include('aplikacja.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('uzytkownicy/', views.uzytkownicy),
    path('uzytkownik_modyfikacja/<int:pk>/', views.uzytkownik_modyfikacja),
    path('uzytkownik_tworzenie/', views.uzytkownik_tworzenie),

    path('zamowienia/', views.zamowienia),
    path('zamowienie_tworzenie/', views.zamowienie_tworzenie),
    path('zamowienie_modyfikacja/<int:pk>/', views.zamowienie_modyfikacja),

    path('produkty/', views.produkty),
    path('produkt_tworzenie/', views.produkt_tworzenie),
    path('produkt_modyfikacja/<int:pk>/', views.produkt_modyfikacja),

    path('koszyki/', views.koszyki),
    path('koszyk_tworzenie/', views.koszyk_tworzenie),
    path('koszyk_modyfikacja/<int:pk>/', views.koszyk_modyfikacja),

    path('zamowienia_zrealizowane/', views.zamowienia_zrealizowane),
    path('uzytkownicy_specjalni/', views.uzytkownicy_specjalni),



    path('rejestracja/', views.rejestracja),

]
