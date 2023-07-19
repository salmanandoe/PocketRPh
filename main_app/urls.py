from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('medications/', views.MedicationList.as_view(), name="medication_list"),
    path('database/', views.PharmacyDatabase.as_view(), name="pharmacy_database"),

]