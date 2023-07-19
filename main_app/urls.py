from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('medications/', views.MedicationList.as_view(), name="medication_list"),
    path('database/', views.PharmacyDatabase.as_view(), name="pharmacy_database"),
    path('medications/new/', views.MedicationCreate.as_view(), name="medication_create"),
    path('medications/<int:pk>/', views.MedicationDetail.as_view(), name="medication_detail"),
    path('medications/<int:pk>/update',views.MedicationUpdate.as_view(), name="medication_update"),
    path('medications/<int:pk>/delete',views.MedicationDelete.as_view(), name="medication_delete"),
]
