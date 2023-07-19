from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"


class Profile(TemplateView):
    template_name = "profile.html"
    

class Medication:
    def __init__(self, image, name, strength, dose, route, frequency, indication):
        self.image = image
        self.name = name
        self.strength = strength
        self.dose = dose
        self.route = route
        self.frequency = frequency
        self.indication = indication

medications = [
    Medication("https://img.freepik.com/free-vector/medicine-capsule-pill-icon-vector_53876-166682.jpg?w=2000", "Metformin", "500 mg", "1000 mg", "by mouth", "twice daily", "diabetes"),
]


class MedicationList(TemplateView):
    template_name = "medication_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medications"] = medications
        return context
        