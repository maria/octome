from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from octo_cv.models import Contact
from octo_site.constants import ContactType


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        social_contacts = Contact.objects.filter(type=ContactType.SOCIAL)
        return render(request, self.template_name, {'social_contacts': social_contacts})
