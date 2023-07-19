from django.urls import reverse
from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Medication
from .models import Database
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


class Home(TemplateView):
    template_name = "home.html"


class Profile(TemplateView):
    template_name = "profile.html"


class MedicationList(TemplateView):
    template_name = "medication_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["medications"] = Medication.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["medications"] = Medication.objects.all()
            context["header"] = "My medications"
        return context  


class PharmacyDatabase(TemplateView):
    template_name = "pharmacy_database.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        generic_name = self.request.GET.get("generic_name")
        if generic_name != None:
            context["database"] = Database.objects.filter(generic_name__icontains=generic_name)
            context["header"] = f"Searching for {generic_name}"
        else: 
            context["database"] = Database.objects.all()
            context["header"] = "Search the pharmacy database"
        return context
        

class MedicationCreate(CreateView):
    model = Medication
    fields = ['img', 'name', 'strength', 'dose', 'route', 'frequency', 'indication']
    template_name = "medication_create.html"
    
    def get_success_url(self):
        return reverse('medication_detail', kwargs={'pk': self.object.pk})
    

class MedicationDetail(DetailView):
    model = Medication
    template_name = "medication_detail.html"


class MedicationUpdate(UpdateView):
    model = Medication
    fields = ['img', 'name', 'strength', 'dose', 'route', 'frequency', 'indication']
    template_name = "medication_update.html"
    
    def get_success_url(self):
        return reverse('medication_detail', kwargs={'pk': self.object.pk})
    

class MedicationDelete(DeleteView):
    model = Medication
    template_name = "medication_delete_confirmation.html"
    success_url = "/medications/"

    

