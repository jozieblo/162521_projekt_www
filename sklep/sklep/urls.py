from django.contrib import admin
from django.urls import path, include
from aplikacja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplikacja/', include('aplikacja.urls')),
    path('uzytkownicy/', views.uzytkownicy),
]
